from utils import ensure_success, ensure_failure

from amtrak.validators.station import Station
from pydantic import TypeAdapter

ta = TypeAdapter(Station)

def test_validator():
    ensure_success("ABC", ta)

def test_length_validator():
    blacklist = ["AB", "ABCD"]
    message = "Assertion failed, station codes must be 3 characters long"
    ensure_failure(blacklist, ta, message)

def test_alpha_validator():
    blacklist = ["AB1", "123", "AB ", "   ", "A.B"]
    message = "Assertion failed, station codes must be alphabetical"
    ensure_failure(blacklist, ta, message)

def test_case_validator():
    blacklist = ["abc", "aBc", "abC", "aBC", "Abc", "ABc", "AbC", "ABc"]
    message = "Assertion failed, station codes must be uppercase"
    ensure_failure(blacklist, ta, message)