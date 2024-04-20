from pydantic import (
    BaseModel,
    AliasChoices,
    Field,
    field_validator,
)

from typing import Optional

from amtrak.api.date import get_timezone_from_character

from amtrak.types import (
    StationCode,
    LocalizedEvent,
)

NONE_STRING_FIELDS = [
    "scheduled_arrival",
    "scheduled_departure",
    "estimated_arrival",
    "estimated_departure",
    "post_arrival",
    "post_departure",
    "schedule_note",
    "post_note",
    "arrival_note",
    "departure_note"
]

class Stop(BaseModel):
    station: StationCode = Field(validation_alias = AliasChoices("station", "station_code", "code"))
    timezone: str = Field(validation_alias = AliasChoices("tz", "timezone"))
    
    # Whether the service is a bus or train
    is_bus: bool = Field(validation_alias = AliasChoices("bus", "is_bus"))
    
    # Automation
    # These fields help to understand whether the arrival and departure
    # times are manually entered or if they are generated automatically
    # by a system or software.
    automated_arrival: bool = Field(validation_alias = AliasChoices("autoarr", "automated_arrival"))
    automated_departure: bool = Field(validation_alias = AliasChoices("autodep", "automated_departure"))
    
    # Post arrival/departure (previous stop)
    post_arrival: Optional[LocalizedEvent] = Field(default = None, validation_alias = AliasChoices("postarr", "post_arrival"))
    post_departure: Optional[LocalizedEvent] = Field(default = None, validation_alias = AliasChoices("postdep", "post_departure"))
    
    # Scheduled arrival/departure
    scheduled_arrival: Optional[LocalizedEvent] = Field(default = None, validation_alias = AliasChoices("scharr", "scheduled_arrival"))
    scheduled_departure: Optional[LocalizedEvent] = Field(default = None, validation_alias = AliasChoices("schdep", "scheduled_departure"))
    
    # Estimated arrival/departure
    estimated_arrival: Optional[LocalizedEvent] = Field(default = None, validation_alias = AliasChoices("estarr", "estimated_arrival"))
    estimated_departure: Optional[LocalizedEvent] = Field(default = None, validation_alias = AliasChoices("estdep", "estimated_departure"))
    
    # Notes
    schedule_note: Optional[str] = Field(default = None, validation_alias = AliasChoices("schcmnt", "schedule_note"))
    post_note: Optional[str] = Field(default = None, validation_alias = AliasChoices("postcmnt", "post_note"))
    arrival_note: Optional[str] = Field(default = None, validation_alias = AliasChoices("estarrcmnt", "arrival_note"))
    departure_note: Optional[str] = Field(default = None, validation_alias = AliasChoices("estdepcmnt", "departure_note"))
    
    @field_validator(*NONE_STRING_FIELDS, mode = "before")
    def convert_none_str(cls, v):
        if v == "" or v is None:
            return None
        return v

    @field_validator("timezone", mode = "before")
    def parse_timezone(cls, v):
        if len(v) == 1:
            return get_timezone_from_character(v)
        return v