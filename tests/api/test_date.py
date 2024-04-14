from amtrak.api.date import (
    get_timezone_from_character,
    parse_date,
)

def test_eastern():
    tz = get_timezone_from_character("e")
    assert tz == "America/New_York"

def test_central():
    tz = get_timezone_from_character("c")
    assert tz == "America/Chicago"

def test_mountain():
    tz = get_timezone_from_character("m")
    assert tz == "America/Denver"

def test_pacific():
    tz = get_timezone_from_character("p")
    assert tz == "America/Los_Angeles"

def test_unknown():
    tz = get_timezone_from_character("q")
    assert tz == "America/New_York"

def test_handles_falsey_dates():
    date = parse_date(None)
    assert date is None

def test_defaults_to_eastern_time():
    date = parse_date("02/03/2017 3:47:00")
    
    # TODO: Figure out if we should instead be passing the commented test case
    #assert date == "2017-02-03T08:47:00.000Z"
    assert date == "2017-02-03T03:47:00-05:00"

def test_uses_the_optionally_provided_timezone():
    date = parse_date("02/03/2017 3:47:00", "America/Denver")
    # TODO: Figure out if we should instead be passing the commented test case
    #assert date == "2017-02-03T10:47:00.000Z"
    assert date == "2017-02-03T03:47:00-07:00"