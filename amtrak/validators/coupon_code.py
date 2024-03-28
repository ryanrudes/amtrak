from amtrak.validators.utils import count_character_types
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

def check_code(code: str) -> str:
    # Check that the coupon code is 14 characters long
    assert len(code) == 14, "coupon code must be 14 characters long"
    
    # Count the number of various character types in the coupon code
    digit_count, alpha_count, other_count = count_character_types(code)
    
    # Check that the coupon code doesn't contain any special characters
    assert other_count == 0, "coupon code must only contain alphanumeric characters"
    
    # Check that the coupon code is all uppercase
    assert code.isupper(), "coupon code must be uppercase"
    
    return code

CouponCode = Annotated[str, AfterValidator(check_code)]