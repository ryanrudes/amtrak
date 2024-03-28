from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

def check_code(code: str) -> str:
    assert len(code) == 3, "station codes must be 3 characters long"
    assert code.isalpha(), "station codes must be alphabetical"
    assert code.isupper(), "station codes must be uppercase"
    return code
    
Station = Annotated[str, AfterValidator(check_code)]