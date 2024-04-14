# TODO: _id and gx_id might always be the same
# TODO: make these events PastEvent types
# TODO: address lat/lon vs coordinates
# TODO: localize departure time to timezone

import pytz

from pydantic import (
    BaseModel,
    AliasChoices,
    Field,
    NonNegativeFloat,
    field_validator,
)

from typing import Optional, Union, List

from datetime import datetime

from amtrak.api.date import get_timezone_from_character

from amtrak.enums import (
    Compass,
    TrainState,
)

from amtrak.types import (
    Identifier,
    ObjectID,
    CMSID,
    GXID,
    Heading,
    Longitude,
    Latitude,
    StationCode,
    Event,
    LocalizedEvent,
    TrainNumber,
    Velocity,
)

NONE_STRING_FIELDS = [
    "event",
    "status",
    "velocity",
    "heading",
    "status",
    "view_station1",
    "view_station2"
]

class Train(BaseModel):
    # Identifiers
    _id: Identifier
    object_id: ObjectID = Field(validation_alias = AliasChoices("OBJECTID", "object_id"))
    cms_id: CMSID = Field(validation_alias = AliasChoices("CMSID", "cms_id"))
    gx_id: GXID
    
    # Coordinates
    longitude: Longitude = Field(validation_alias = AliasChoices("lon", "longitude"))
    latitude: Latitude = Field(validation_alias = AliasChoices("lat", "latitude"))
    
    # Codes
    event: Optional[StationCode] = Field(validation_alias = AliasChoices("EventCode", "event"))
    origin: StationCode = Field(validation_alias = AliasChoices("OrigCode", "origin"))
    destination: StationCode = Field(validation_alias = AliasChoices("DestCode", "destination"))
    
    # Events
    created_at: Event
    updated_at: Event
    
    # Departure
    departure: LocalizedEvent = Field(validation_alias = AliasChoices("OrigSchDep", "departure"))
    timezone: str = Field(validation_alias = AliasChoices("OriginTZ", "timezone"))
        
    # Velocity and heading of the train
    velocity: Optional[Velocity] = Field(validation_alias = AliasChoices("Velocity", "velocity", "speed"))
    heading: Optional[Heading] = Field(validation_alias = AliasChoices("Heading", "heading", "direction"),)

    # Route name
    route: str = Field(validation_alias = AliasChoices("RouteName", "route"))
    
    # Train number
    number: TrainNumber = Field(validation_alias = AliasChoices("TrainNum", "number"))
    
    # Train state
    state: TrainState = Field(validation_alias = AliasChoices("TrainState", "state"))
    
    # Aliases
    aliases: List[int] = Field(validation_alias = AliasChoices("Aliases", "aliases"))
    
    # Status message
    status: Optional[str] = Field(validation_alias = AliasChoices("StatusMsg", "status"))
    
    # View Station
    view_station1: Optional[Event] = Field(validation_alias = AliasChoices("ViewStn1", "view_station1"))
    view_station2: Optional[Event] = Field(validation_alias = AliasChoices("ViewStn2", "view_station2"))
    
    # Unsure
    last_val_timestamp: Optional[Event] = Field(validation_alias = AliasChoices("LastValTS", "last_val_timestamp"))
    
    @property
    def speed(self) -> Optional[Velocity]:
        """Alias for velocity"""
        if self.velocity is None:
            return None
        
        return self.velocity
    
    @field_validator(*NONE_STRING_FIELDS, mode = "before")
    def convert_none_str(cls, v):
        if v == "None" or v is None:
            return None
        return v

    @field_validator("aliases", mode = "before")
    def validate_aliases(cls, v):
        if v == "None" or v is None:
            return []
        elif isinstance(v, list):
            return v
        elif isinstance(v, str):
            return [] if v == '' else v.split(',')
        else:
            raise TypeError("aliases must be a string or list of strings")
    
    @field_validator("timezone", mode = "before")
    def parse_timezone(cls, v):
        if len(v) == 1:
            return get_timezone_from_character(v)
        return v