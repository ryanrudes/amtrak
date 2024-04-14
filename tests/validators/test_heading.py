from utils import ensure_success, ensure_failure

from amtrak.types import Heading#, NoneStringField
from pydantic import TypeAdapter, ValidationError
from typing import Optional

def test_heading():
    whitelist = ["N", "S", "E", "W",
                 "n", "s", "e", "w",
                 "NE", "NW", "SE", "SW",
                 "ne", "nw", "se", "sw",
                 "north", "south", "east", "west",
                 "North", "South", "East", "West",
                 "northeast", "northwest", "southeast", "southwest",
                 "Northeast", "Northwest", "Southeast", "Southwest",
                 "north east", "south west", "south east", "south west",
                 "North East", "South West", "South East", "South West",]
    
    blacklist = ["F", "NF", "feast", "eastnorth", "Mouth Eat"]
    
    ta = TypeAdapter(Heading)
    
    ensure_success(whitelist, ta)
    ensure_failure(blacklist, ta)
    
    assert ta.validate_python("N") == ta.validate_python("north")
    assert ta.validate_python("S") == ta.validate_python("south")
    assert ta.validate_python("E") == ta.validate_python("east")
    assert ta.validate_python("W") == ta.validate_python("west")
    
    assert ta.validate_python("NE") == ta.validate_python("northeast") == ta.validate_python("north east")
    assert ta.validate_python("NW") == ta.validate_python("northwest") == ta.validate_python("north west")
    assert ta.validate_python("SE") == ta.validate_python("southeast") == ta.validate_python("south east")
    assert ta.validate_python("SW") == ta.validate_python("southwest") == ta.validate_python("south west")

"""
def test_optional_heading():
    from pydantic import BaseModel

    class ThingWithOptionalHeading(BaseModel):
        heading: Optional[Heading] = NoneStringField()
        
    print(ThingWithOptionalHeading.model_validate({"heading": "None"}).heading)
"""