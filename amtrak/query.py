from amtrak.validators.utils import validate_passenger_counts
from amtrak.validators import StationCode, Traveler, Travelers, PromoCode, CouponCode
from amtrak.enums import AgeGroup, Discount

from pydantic import BaseModel, model_validator

from typing import Optional
from datetime import date
from warnings import warn

class Query(BaseModel):
    # Specify the origin and destination stations
    origin: StationCode
    destination: StationCode
    # Specify the number of passengers by age group
    adults: int = 0
    seniors: int = 0
    youth: int = 0
    children: int = 0
    infants: int = 0
    # Specify the travelers directly
    travelers: Optional[Travelers] = None
    # Specify if any passengers need assistance or have a disability
    needs_assistance: bool = False
    # Specify the promo code and/or coupon code
    promo_code: Optional[PromoCode] = None
    coupon_code: Optional[CouponCode] = None
    # Specify the departure and return dates
    depart_date: date
    return_date: date
    
    @model_validator(mode = "after")
    def check_query(self):
        # TODO: Implement assistance/disability support
        assert not self.needs_assistance, "assistance/disability support is not yet implemented"
        
        # Validate travelers
        specified_passenger_counts = self.adults + self.seniors + self.youth + self.children + self.infants > 0
        specified_travelers = self.travelers is not None
            
        if specified_travelers:
            assert not specified_passenger_counts, "passenger counts and travelers are mutually exclusive; either specify passenger counts or travelers, not both"
            
            # Count the number of passengers from each age group
            self.adults = 0
            self.seniors = 0
            self.youth = 0
            self.children = 0
            self.infants = 0
            
            for traveler in self.travelers:
                match traveler.age:
                    case AgeGroup.ADULT:
                        self.adults += 1
                    case AgeGroup.SENIOR:
                        self.seniors += 1
                    case AgeGroup.YOUTH:
                        self.youth += 1
                    case AgeGroup.CHILD:
                        self.children += 1
                    case AgeGroup.INFANT:
                        self.infants += 1
        else:
            assert specified_passenger_counts, "must specify either passenger counts or travelers"
            
            validate_passenger_counts(self.adults, self.seniors, self.youth, self.children, self.infants)
            
            travelers = []
            
            for _ in range(self.adults):
                adult_traveler = Traveler(age = AgeGroup.ADULT, discount = Discount.ADULT)
                travelers.append(adult_traveler)
                
            for _ in range(self.seniors):
                senior_traveler = Traveler(age = AgeGroup.SENIOR, discount = Discount.SENIOR)
                travelers.append(senior_traveler)
                
            for _ in range(self.youth):
                youth_traveler = Traveler(age = AgeGroup.YOUTH, discount = Discount.YOUTH)
                travelers.append(youth_traveler)
                
            for _ in range(self.children):
                child_traveler = Traveler(age = AgeGroup.CHILD, discount = Discount.CHILD)
                travelers.append(child_traveler)
                
            for _ in range(self.infants):
                infant_traveler = Traveler(age = AgeGroup.INFANT, discount = Discount.INFANT)
                travelers.append(infant_traveler)
            
            self.travelers = travelers
        
        # TODO: Support discounted travel
        # Warn about non-default discounts
        for traveler in self.travelers:
            if traveler.discount != traveler.age.default_discount:
                warn("Discounted travel is not yet supported")

        self.travelers = Travelers(travelers = self.travelers)
            
        return self