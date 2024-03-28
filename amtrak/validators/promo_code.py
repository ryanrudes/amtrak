from amtrak.validators.utils import count_character_types
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

def check_code(code: str) -> str:
    # Check that the promo code is 4 characters long
    assert len(code) == 4, "promo code must be 4 characters long"
    
    # Count the number of various character types in the promo code
    digit_count, alpha_count, other_count = count_character_types(code)
    
    # Check that the promo code doesn't contain any special characters
    assert other_count == 0, "promo code must only contain alphanumeric characters"
    
    # Check that the promo code contains both letters and digits
    assert alpha_count > 0 and digit_count > 0, "promo code must contain both letters and digits"
    
    # Check that the promo code is all uppercase
    assert code.isupper(), "promo code must be uppercase"
    
    return code

PromoCode = Annotated[str, AfterValidator(check_code)]