from utils import ensure_success, ensure_failure

from amtrak.validators.coupon_code import CouponCode
from pydantic import TypeAdapter

ta = TypeAdapter(CouponCode)

def test_coupon_code_validator():
    whitelist = ["AMTRAKDISCOUNT", "AMTRAKD1SCOUNT", "AMTRAKDISC0UNT", "AMTRAKD1SC0UNT"]
    ensure_success(whitelist, ta)
    
def test_length_validator():
    blacklist = ["AMTRAK", "DISCOUNTEDAMTRAKTICKETS"]
    message = "Assertion failed, coupon code must be 14 characters long"
    ensure_failure(blacklist, ta, message)

def test_alphanumeric_validator():
    blacklist = ["ILOVEA!MTRAK12", "ABCDEFG?HIJKLM"]
    message = "Assertion failed, coupon code must only contain alphanumeric characters"
    ensure_failure(blacklist, ta, message)

def test_case_validator():
    blacklist = ["amtrakdiscount", "AmtrakDiscount", "amtrakDiscount"]
    message = "Assertion failed, coupon code must be uppercase"
    ensure_failure(blacklist, ta, message)