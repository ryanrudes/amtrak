from amtrak.api.endpoints.stations import get_stations
from amtrak.api.crypto import get_crypto_initializers
from amtrak.validators import Feature
from amtrak.enums import StationType

from unittest.mock import Mock, patch
from datetime import datetime

# TODO: Use mocks more approperately

with patch("requests.get") as mock_get, patch("amtrak.api.crypto.parse") as mock_parse:    
    # Create mockup for requests.get
    mock1 = Mock()
    mock1.json.return_value = []

    s = "12345678"
    v = "12345678901234567890123456789012"
    
    payload = dict(
        arr = ["0b1d2897-640a-4c64-a1d8-b54f453a7ad7"],
        s = [s] * 8 + ["deadbeef"],
        v = [v] * 32 + ["7e117a1e7e117a1e7e117a1e7e117a1e"],
    )
    
    mock2 = Mock()
    mock2.json.return_value = payload

    mock3 = Mock()
    mock3.text = "this is some text"
    
    def side_effect(url, *args, **kwargs):
        match url:
            case "https://maps.amtrak.com/rttl/js/RoutesList.json":
                return mock1
            case "https://maps.amtrak.com/rttl/js/RoutesList.v.json":
                return mock2
            case "https://maps.amtrak.com/services/MapDataService/stations/trainStations":
                return mock3

    mock_get.side_effect = side_effect
    
    # Create mockup for parse function
    payload = {
        "StationsDataResponse": {
            "features": [
                {
                    "properties": {
                        "OBJECTID": 1,
                        "lon": -121.816,
                        "lat": 38.018,
                        "IsTrainSt": "Y",
                        "MapZmLvl": "5",
                        "gx_id": "ACA",
                        "DateModif": "2017-11-06T07:04:20",
                        "StaType": "Platform with Shelter",
                        "Zipcode": "12345",
                        "State": "FR",
                        "City": "Cityville",
                        "Address1": "Street 1",
                        "Address2": "Unit 1",
                        "Name": "",
                        "Code": "STA",
                        "created_at": "3/27/2024 5:00:36 AM",
                        "updated_at": "3/27/2024 5:00:36 AM",
                        "StationName": "Station 1",
                        "StationFacilityName": "",
                        "StationAliases": "Station One",
                        "StationRank": "",
                    },
                },
                {
                   "properties": {
                        "OBJECTID": 1,
                        "lon": 21.816,
                        "lat": -38.018,
                        "IsTrainSt": "N",
                        "MapZmLvl": "3",
                        "gx_id": "BDB",
                        "DateModif": "2018-06-21T03:05:26",
                        "StaType": "Curbside Bus Stop only (no shelter)",
                        "Zipcode": "54321",
                        "State": "AL",
                        "City": "Metropolis",
                        "Address1": "Street 2",
                        "Address2": "Unit 2",
                        "Name": "",
                        "Code": "STB",
                        "created_at": "4/17/2023 3:15:27 AM",
                        "updated_at": "4/1/2024 6:12:45 PM",
                        "StationName": "Station 2",
                        "StationFacilityName": "",
                        "StationAliases": "Station Two,Station Too",
                        "StationRank": "2",
                    },
                },
            ],
        },
    }
    
    mock_parse.return_value = payload
    
    def test_maps_stations_into_our_lingo():
        out = get_stations(crypto_parse = mock_parse, fetch = mock_get)
        
        expected_output = [
            Feature(
                object_id = 1,
                longitude = -121.816,
                latitude = 38.018,
                is_train_station = True,
                zoom = 5,
                gx_id = "ACA",
                date_modified = datetime(2017, 11, 6, 7, 4, 20),
                station_type = StationType.PLATFORM_WITH_SHELTER,
                zip_code = "12345",
                state = "FR",
                city = "Cityville",
                address1 = "Street 1",
                address2 = "Unit 1",
                name = None,
                code = "STA",
                created_at = datetime(2024, 3, 27, 5, 0, 36),
                updated_at = datetime(2024, 3, 27, 5, 0, 36),
                station_name = "Station 1",
                station_facility_name = None,
                station_aliases = ["Station One"],
                station_rank = None,
            ),
            Feature(
                object_id = 1,
                longitude = 21.816,
                latitude = -38.018,
                is_train_station = False,
                zoom = 3,
                gx_id = "BDB",
                date_modified = datetime(2018, 6, 21, 3, 5, 26),
                station_type = StationType.CURBSIDE,
                zip_code = "54321",
                state = "AL",
                city = "Metropolis",
                address1 = "Street 2",
                address2 = "Unit 2",
                name = None,
                code = "STB",
                created_at = datetime(2023, 4, 17, 3, 15, 27),
                updated_at = datetime(2024, 4, 1, 18, 12, 45),
                station_name = "Station 2",
                station_facility_name = None,
                station_aliases = ["Station Two", "Station Too"],
                station_rank = 2,
            ),
        ]
        
        assert out == expected_output