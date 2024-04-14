from pydantic import TypeAdapter, ValidationError
from typing import Union, Optional
from json import dumps

def ensure_success(whitelist: Union[str, list[str]], ta: TypeAdapter):
    if not isinstance(whitelist, list):
        whitelist = [whitelist]
        
    for item in whitelist:
        ta.validate_python(item)
        
def ensure_failure(blacklist: Union[str, list[str]], ta: TypeAdapter, expected_message: Optional[str] = None):
    if not isinstance(blacklist, list):
        blacklist = [blacklist]
        
    for item in blacklist:
        try:
            ta.validate_python(item)
            assert False, "expected validation error"
        except ValidationError as exc:
            errors = exc.errors()
            assert len(errors) == 1, "expected 1 error"
            
            if expected_message is not None:
                error_message = errors[0]["msg"]
                assert error_message == expected_message, "unexpected error message"
    
def ensure_field_failure(blacklist: Union[str, list[str]], ta: TypeAdapter, payload: dict, field: str, expected_message: Optional[str] = None):
    if not isinstance(blacklist, list):
        blacklist = [blacklist]
        
    for item in blacklist:
        payload[field] = item

        try:
            ta.validate_json(dumps(payload))
            assert False, "expected validation error"
        except ValidationError as exc:
            errors = exc.errors()
            assert len(errors) == 1, "expected 1 error"
            
            if expected_message is not None:
                error_message = errors[0]["msg"]
                assert error_message == expected_message, "unexpected error message"