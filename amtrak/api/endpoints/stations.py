from amtrak.validators.feature import Feature
from amtrak.api.crypto import parse

import requests

def get_stations(crypto_parse = parse, fetch = requests.get) -> [Feature]:
    endpoint = "https://maps.amtrak.com/services/MapDataService/stations/trainStations"
    response = fetch(endpoint)

    # Decrypt the stations
    stations = crypto_parse(response.text)
    features = []
    
    for feature in stations["StationsDataResponse"]["features"]:
        properties = feature["properties"]
        feature = Feature(**properties)
        features.append(feature)
        
    return features