from amtrak import API

# Initialize the API
api = API()

def test_get_stations():
    """
    Test the get_stations method.
    """
    # Retrieve the stations
    stations = api.get_stations()
    
    # Ensure the stations are not empty
    assert len(stations) > 0