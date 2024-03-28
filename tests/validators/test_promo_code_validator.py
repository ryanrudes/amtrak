from utils import ensure_success, ensure_failure

from amtrak.validators.promo_code import PromoCode
from pydantic import TypeAdapter

ta = TypeAdapter(PromoCode)

def test_promo_code_validator():
    whitelist = ["C0ST", "S1CK", "D1SC", "A12B", "123A"]
    ensure_success(whitelist, ta)
    
def test_length_validator():
    blacklist = ["TIX", "AMTRAK", "DISCOUNTEDAMTRAKTICKETS"]
    message = "Assertion failed, promo code must be 4 characters long"
    ensure_failure(blacklist, ta, message)

def test_special_characters_validator():
    blacklist = ["HEY!", "D!SC"]
    message = "Assertion failed, promo code must only contain alphanumeric characters"
    ensure_failure(blacklist, ta, message)
    
def test_alphanumeric_validator():
    blacklist = ["ABCD", "1234"]
    message = "Assertion failed, promo code must contain both letters and digits"
    ensure_failure(blacklist, ta, message)

def test_case_validator():
    blacklist = ["c0st", "C0st", "C0st", "C0St", "C0St"]
    message = "Assertion failed, promo code must be uppercase"
    ensure_failure(blacklist, ta, message)