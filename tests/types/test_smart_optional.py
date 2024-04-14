# TODO: perhaps remove this

from amtrak.types import Event
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

class StrModel(BaseModel):
    field: Optional[str]

    @field_validator("field", mode = "before")
    def convert_none_str(cls, v):
        if v == "None":
            return None
        return v

class EventModel(BaseModel):
    field: Optional[Event]

    @field_validator("field", mode = "before")
    def convert_none_str(cls, v):
        if v == "None":
            return None
        return v
    
def test_smart_optional():
    model = StrModel(field = "None")
    assert model.field is None
    model = StrModel(field = None)
    assert model.field is None
    model = StrModel(field = "none")
    assert model.field is not None
    
    model = EventModel(field = "None")
    assert model.field is None
    model = EventModel(field = None)
    assert model.field is None
    model = EventModel(field = "3/28/2024 4:19:53 PM")
    assert model.field == datetime(2024, 3, 28, 16, 19, 53)