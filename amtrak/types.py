"""Defines all custom type annotations for the project."""

from typing_extensions import Annotated
from typing import TypeVar, Union, Optional, Generic

from datetime import datetime

from pydantic.functional_validators import AfterValidator
from pydantic import (
    BaseModel,
    AliasChoices,
    BeforeValidator,
    Field,
    PastDatetime,
    FutureDatetime,
    PositiveInt,
    NonNegativeFloat,
    field_validator,
)

from amtrak.enums import (
    Compass,
)

# Station code
def check_station_code(code: str) -> str:
    assert len(code) == 3, "station codes must be 3 characters long"
    assert code.isalpha(), "station codes must be alphabetical"
    assert code.isupper(), "station codes must be uppercase"
    return code

StationCode = Annotated[str,
    Field(
        min_length = 3,
        max_length = 3,
        pattern = "^[A-Z]{3}$",
        title = "Station Code",
        description = "The 3-letter identifier for the station.",
        examples = ["NYP", "WAS", "PHL"],
    ),
    AfterValidator(check_station_code),
]

# Longitude
Longitude = Annotated[float,
    Field(
        ge = -180,
        le = +180,
        title = "Longitude",
        description = "The longitude of the station.",
        examples = [-73.997070, -77.005676, -75.181953],
    ),
]

# Latitude
Latitude = Annotated[float,
    Field(
        ge = -90,
        le = +90,
        title = "Latitude",
        description = "The latitude of the station.",
        examples = [40.751282, 38.896042, 39.955730],
    )
]

# Zip Code
AmericanZipCode = Annotated[str,
    Field(
        min_length = 5,
        max_length = 5,
        pattern = r"^\d{5}$",
        title = "US Postal Code",
        description = "The postal code for a US station.",
        examples = ["10001", "20002", "19104"],
    )
]

CanadianZipCode = Annotated[str,
    Field(
        pattern = r"^[A-Z]\d[A-Z]\s\d[A-Z]\d$",
        title = "Canadian Postal Code",
        description = "The postal code for a Canadian station.",
        examples = ["M5V 1J9", "K1A 0B1", "V6C 3E3"],
    )
]

ZipCode = Union[AmericanZipCode, CanadianZipCode]

# State
State = Annotated[str,
    Field(
        min_length = 2,
        max_length = 2,
        pattern = "^[A-Z]{2}$",
        title = "State",
        description = "The 2-letter abbreviation for the state or province of the station.",
        examples = ["NY", "PA", "DC"],
    )
]

# ID: 7 digit number
Identifier = Annotated[str,
    Field(
        min_length = 7,
        max_length = 7,
        pattern = r"^\d{7}$",
        title = "Identifier",
        description = "A 7-digit identifier.",
        examples = ["1234567", "9876543", "4567890"],
    )
]

# Object Identifier
ObjectID = Annotated[PositiveInt,
    Field(
        title = "Object Identifier",
        description = "The unique identifier for the object.",
        examples = [1, 2, 3],
    )
]

# Event
# TODO: This is written really poorly
def parse_event(dt: str) -> datetime:
    try:
        return datetime.strptime(dt, "%m/%d/%Y %I:%M:%S %p")
    except:
        return datetime.strptime(dt, "%m/%d/%Y %H:%M:%S")
        
Event = Annotated[datetime,
    BeforeValidator(parse_event),
    Field(
        title = "Event",
        description = "The date and time of the event.",
        examples = ["3/28/2024 7:31:47 PM", "10/2/2024 12:04:28 AM"],
    )
]

# TODO: Most implementations of this aren't actually localized yet
LocalizedEvent = Annotated[datetime,
    BeforeValidator(parse_event),
    Field(
        title = "Localized Event",
        description = "The date and time of the event in the local timezone.",
        examples = ["3/28/2024 7:31:47 PM", "10/2/2024 12:04:28 AM"],
    )
]

# Velocity
Velocity = Annotated[NonNegativeFloat,
    Field(
        ge = 0,
        title = "Velocity",
        description = "The velocity of the train.",
        examples = [0.0, 10.0, 20.0],
    )
]

# Origin
# timezone
# scheduled_departure
# code

# Train Number
TrainNumber = Annotated[PositiveInt,
    Field(
        title = "Train Number",
        description = "The unique number of the train.",
        examples = [1, 2, 3],
    )
]

# CMS ID: 13 digit number
CMSID = Annotated[str,
    Field(
        min_length = 13,
        max_length = 13,
        pattern = r"^\d{13}$",
        title = "CMS Identifier",
        description = "The 13-digit identifier for the CMS.",
        examples = ["1234567890123", "9876543210987", "4567890123456"],
    )
]

# GX ID: 7 digit number
GXID = Annotated[str,
    Field(
        min_length = 7,
        max_length = 7,
        pattern = r"^\d{7}$",
        title = "GX Identifier",
        description = "The 7-digit identifier for the GX.",
        examples = ["1234567", "9876543", "4567890"],
    )
]

# Heading
heading_abbreviations = {
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "NORTHEAST": "NE",
    "NORTHWEST": "NW",
    "SOUTHEAST": "SE",
    "SOUTHWEST": "SW",
}

def validate_heading(direction: Optional[Union[str, Compass]]) -> Optional[Compass]:
    if direction == "None" or direction is None:
        return None
    elif isinstance(direction, str):
        
        direction = direction.upper().strip().replace(' ', '')
        
        if direction in heading_abbreviations.keys():
            direction = heading_abbreviations[direction]
        elif direction not in heading_abbreviations.values():
            raise ValueError("unrecognized direction")
        
        direction = Compass(direction)
    elif not isinstance(direction, Compass):
        raise TypeError("heading must be a string or Direction")
    
    return direction
        
Heading = Annotated[Compass,
    BeforeValidator(validate_heading),
    Field(
        default = None,
        title = "Heading",
        description = "The direction the train is heading.",
        examples = ["N", "S", "E", "W",
                    "NE", "NW", "SE", "SW",
                    "north", "south", "east", "west",
                    "northeast", "northwest", "southeast", "southwest"],
    )
]