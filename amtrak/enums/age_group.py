from amtrak.enums.discount import Discount
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
    
    @property
    def default_discount(self) -> Discount:
        """Get the default discount for the age group.
        
        Returns:
            Discount: The default discount for the age group.
        """
        match self:
            case AgeGroup.ADULT:
                return Discount.ADULT
            case AgeGroup.SENIOR:
                return Discount.SENIOR
            case AgeGroup.YOUTH:
                return Discount.YOUTH
            case AgeGroup.CHILD:
                return Discount.CHILD
            case AgeGroup.INFANT:
                return Discount.INFANT