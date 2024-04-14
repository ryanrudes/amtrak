from enum import Enum

# TODO: implement function that gets intermediate of two primary cardinal directions
# NOTE: `Compass` is the Enum, `Heading` is the type

class Compass(Enum):
    """
    Enumeration representing cardinal and secondary directions.
    
    This enumeration provides a set of constants representing the primary cardinal directions
    (NORTH, SOUTH, EAST, WEST) and the secondary cardinal directions (NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST).
    It also includes aliases for convenience (N, S, E, W) and (NE, NW, SE, SW).
    """
    
    # Primary cardinal directions
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    
    # Secondary cardinal directions
    NORTHEAST = "NE"
    NORTHWEST = "NW"
    SOUTHEAST = "SE"
    SOUTHWEST = "SW"
    
    # Aliases
    N = NORTH
    S = SOUTH
    E = EAST
    W = WEST
    
    NE = NORTHEAST
    NW = NORTHWEST
    SE = SOUTHEAST
    SW = SOUTHWEST