from amtrak.enums import AgeGroup, Discount
from pydantic import BaseModel, model_validator

UNSUPPORTED_DISCOUNTS = [Discount.ADULT_WITH_DISABILITY, Discount.CHILD_WITH_DISABILITY, Discount.COMPANION]

AGE_TO_DISCOUNTS = {
    AgeGroup.ADULT: [Discount.ADULT, Discount.RAIL_PASSENGERS_ASSOCIATION, Discount.MILITARY, Discount.VETERAN],
    AgeGroup.SENIOR: [Discount.SENIOR],
    AgeGroup.YOUTH: [Discount.YOUTH, Discount.RAIL_PASSENGERS_ASSOCIATION, Discount.MILITARY_DEPENDENT],
    AgeGroup.CHILD: [Discount.CHILD, Discount.MILITARY_DEPENDENT],
    AgeGroup.INFANT: [Discount.INFANT],
}

# TODO: Add tests for this validator
class Traveler(BaseModel):
    age: AgeGroup
    discount: Discount
    
    @model_validator(mode = "after")
    def check_discount_applicable(self):
        assert self.discount not in UNSUPPORTED_DISCOUNTS, f"discount \"{self.discount.value}\" is not supported"
        assert self.discount in AGE_TO_DISCOUNTS[self.age], f"Discount \"{self.discount.value}\" is not applicable to age group \"{self.age.value}\""
        return self