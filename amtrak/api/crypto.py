from Crypto.Cipher import AES
from typing import Optional, Callable

import requests
import hashlib
import codecs
import json

# The "private key" embedded in each response is really more of a password used
# to derive a key. Anyway, it's 64 bytes long. Base64 decoded and padded, it
# comes out to 88 bytes. And that's where this number comes from.
MASTER_SEGMENT = 88

def get_crypto_initializers(*, fetch = requests.get) -> tuple[str, bytes, bytes]:
    """Fetch the public key, salt, and AES initialization vector"""
    
    # Fetch the data containing our values
    endpoint = "https://maps.amtrak.com/rttl/js/RoutesList.v.json"
    response = fetch(endpoint)
    crypto_data = response.json()
    
    # The index of the public key is the sum of all zoom levels for all routes
    endpoint = "https://maps.amtrak.com/rttl/js/RoutesList.json"
    response = fetch(endpoint)
    data = response.json()
    master_zoom = sum(item.get("ZoomLevel", 0) for item in data)

    # The public key is the value at the index of the sum of all zoom levels
    key = crypto_data["arr"][master_zoom]
    
    # The salt and IV indices are equal to the length of any given value in the
    # array. So if salt[0] is 8 bytes long, then our value is at salt[8]. Etc.
    num_salt_bytes = len(crypto_data["s"][0])
    num_iv_bytes = len(crypto_data["v"][0])
    
    # Decode the salt and IV from hex
    salt = codecs.decode(crypto_data["s"][num_salt_bytes], "hex")
    iv = codecs.decode(crypto_data["v"][num_iv_bytes], "hex")
    
    return key, salt, iv

def decrypt(
    data: str,
    key_derivation_password: Optional[str] = None,
    *,
    fetch: Callable = requests.get
):
    public_key, salt, iv = get_crypto_initializers(fetch = fetch)
    
    # Decode the content from base64 to binary
    cipher_text = codecs.decode(data.encode(), "base64")
    
    # The actual key is derived from the derivation password using
    # the salt from the API and PBKDS2 with SHA1 (1k iterations and
    # 16-byte output)
    if key_derivation_password is None:
        key_derivation_password = public_key

    key = hashlib.pbkdf2_hmac("sha1", key_derivation_password.encode(), salt, 1000, 16)
    
    # It's encrypted with AES-128-CBC using the generated key above
    # and the hardcoded initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the data and return it as a string
    text = cipher.decrypt(cipher_text)
    return text.decode("utf-8")

def parse(data: str, *, fetch: Callable = requests.get) -> Optional[dict]:
    # The encrypted data is at the beginning. The last 88 bytes are the base64
    # encoded private key password. Slice those two out.
    cipher_text = data[:-MASTER_SEGMENT]
    private_key_cipher = data[-MASTER_SEGMENT:]
    
    # The private key password is encrypted with the public key provided by the
    # API. It's a pipe-delimited string, but only the first segment is useful.
    # We can toss out the rest.
    key_fragments = decrypt(private_key_cipher, fetch = fetch)
    private_key = key_fragments.split('|')[0]
    
    # The actual data is encrypted with the private key. The result is always
    # JSON (for our purposes), so go ahead and parse that.
    # TODO: figure out why random padding is added to the end of the JSON
    plaintext = decrypt(cipher_text, private_key, fetch = fetch)
    # TODO: figure out why random padding is added to the end of the JSON.
    #       this is a quick workaround
    plaintext = plaintext[:plaintext.rindex('}') + 1]
        
    try:
        return json.loads(plaintext)
    except json.JSONDecodeError:
        return None