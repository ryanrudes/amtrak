from enum import Enum

class StationType(Enum):
    PLATFORM = "Platform only (no shelter)"
    STATION = "Station Building (with waiting room)"
    CURBSIDE = "Curbside Bus Stop only (no shelter)"
    PLATFORM_WITH_SHELTER = "Platform with Shelter"