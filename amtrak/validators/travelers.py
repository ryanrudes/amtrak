from pydantic import BaseModel, validator

from amtrak.validators.traveler import Traveler
from amtrak.enums import AgeGroup

# TODO: Add tests for this validator
class Travelers(BaseModel):
    travelers: list[Traveler]
    
    @validator("travelers")
    def perform_checks(cls, travelers):
        # Get the number of adult, child, and infant passengers
        adult_passengers = 0
        child_passengers = 0
        infant_passengers = 0
        
        for traveler in travelers:
            match traveler.age:
                case AgeGroup.ADULT | AgeGroup.SENIOR:
                    adult_passengers += 1
                case AgeGroup.YOUTH | AgeGroup.CHILD:
                    child_passengers += 1
                case AgeGroup.INFANT:
                    infant_passengers += 1
        
        # Check that any passengers were specified
        total_passengers = adult_passengers + child_passengers + infant_passengers
        
        assert total_passengers > 0, "please specify at least one passenger"
        
        # Check that children and infants are accompanied by an adult
        assert adult_passengers > 0, "children must be accompanied by an adult"
        
        # Check that the total number of passengers does not exceed 14
        assert total_passengers <= 14, "cannot book for more than 14 passengers"
        
        # Check that the total number of non-infant passengers does not exceed 8
        non_infant_passengers = total_passengers - infant_passengers
    
        assert non_infant_passengers <= 8, "cannot book for more than 8 non-infant passengers"
        
        return travelers