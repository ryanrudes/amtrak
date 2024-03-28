from enum import Enum

class AgeGroup(Enum):
    """Enum representing different age groups for train travelers.
    
    Attributes:
        ADULT: Represents an adult passenger (age 16+).
        SENIOR: Represents a senior passenger (age 65+).
        YOUTH: Represents a youth passenger (age 13-15).
        CHILD: Represents a child passenger (age 2-12).
        INFANT: Represents an infant passenger (under 2).
    """
    ADULT = "Adult"
    SENIOR = "Senior"
    YOUTH = "Youth"
    CHILD = "Child"
    INFANT = "Infant"