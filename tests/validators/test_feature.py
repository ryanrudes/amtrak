from amtrak.validators.feature import Feature

def test_feature():
    payload = {
        "OBJECTID": 1,
        "lon": -121.816,
        "lat": 38.018,
        "IsTrainSt": "Y",
        "MapZmLvl": "5",
        "gx_id": "ACA",
        "DateModif": "2017-11-06T07:04:20",
        "StaType": "Platform with Shelter",
        "Zipcode": "12345",
        "State": "CA",
        "City": "Antloch",
        "Address1": "100 I Street",
        "Address2": "",
        "Name": "",
        "Code": "ACA",
        "created_at": "3/27/2024 5:00:36 AM",
        "updated_at": "3/27/2024 5:00:36 AM",
        "StationName": "Birmingham, AL",
        "StationFacilityName": "",
        "StationAliases": "Pittsburgh,British Columbia",
        "StationRank": "",
    }
    
    feature = Feature(**payload)
    print(feature.station_rank)