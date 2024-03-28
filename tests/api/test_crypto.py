from amtrak.api.crypto import get_crypto_initializers, parse
from unittest.mock import Mock, patch

import requests

with patch("requests.get") as mock_get:
    mock1 = Mock()
    mock1.json.return_value = []

    s = "12345678"
    v = "12345678901234567890123456789012"
    
    payload = dict(
        arr = ["0b1d2897-640a-4c64-a1d8-b54f453a7ad7"],
        s = [s] * 8 + ["deadbeef"],
        v = [v] * 32 + ["7e117a1e7e117a1e7e117a1e7e117a1e"],
    )
    
    mock2 = Mock()
    mock2.json.return_value = payload

    def side_effect(url, *args, **kwargs):
        match url:
            case "https://maps.amtrak.com/rttl/js/RoutesList.json":
                return mock1
            case "https://maps.amtrak.com/rttl/js/RoutesList.v.json":
                return mock2

    mock_get.side_effect = side_effect

def test_fetch_crypto_initializers():
    key, salt, iv = get_crypto_initializers(fetch = mock_get)
    
    assert key == "0b1d2897-640a-4c64-a1d8-b54f453a7ad7"
    assert salt.hex() == "deadbeef"
    assert iv.hex() == "7e117a1e7e117a1e7e117a1e7e117a1e"
    
def test_parse_encrypted_string():
    parsed_message = parse("9REEYi/JXW52zpVxlbzDP/zQ2NxJE8ykzOdkuiiLn8U0PskEpazNwyQIpmOBlJthSQeY8NhCd9gldfh7C/CscgnbFUD7IHkKaK4fnwB6tyY1C5vh4yZ8rUj5NmPMHCM9G2d/zqKvBZw3iXZFjg18Jw==",
                           fetch = mock_get)
    assert parsed_message == {'a': 'message', 'for': 'the emperor'}