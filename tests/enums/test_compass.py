from amtrak.enums import Compass

def test_compass():
    assert Compass.NORTH == Compass.N
    assert Compass.SOUTH == Compass.S
    assert Compass.EAST == Compass.E
    assert Compass.WEST == Compass.W
    
    assert Compass.NORTHEAST == Compass.NE
    assert Compass.NORTHWEST == Compass.NW
    assert Compass.SOUTHEAST == Compass.SE
    assert Compass.SOUTHWEST == Compass.SW
    
    assert Compass.NORTH.value == Compass.N.value == "N"
    assert Compass.SOUTH.value == Compass.S.value == "S"
    assert Compass.EAST.value == Compass.E.value == "E"
    assert Compass.WEST.value == Compass.W.value == "W"
    
    assert Compass.NORTHEAST.value == Compass.NE.value == "NE"
    assert Compass.NORTHWEST.value == Compass.NW.value == "NW"
    assert Compass.SOUTHEAST.value == Compass.SE.value == "SE"
    assert Compass.SOUTHWEST.value == Compass.SW.value == "SW"