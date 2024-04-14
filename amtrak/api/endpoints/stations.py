from amtrak.objects.station import Station
from amtrak.api.crypto import parse

import requests

def get_stations(crypto_parse = parse, fetch = requests.get) -> [Station]:
    endpoint = "https://maps.amtrak.com/services/MapDataService/stations/trainStations"
    response = fetch(endpoint)

    # Decrypt the stations
    stations = crypto_parse(response.text)
    features = []
    
    for feature in stations["StationsDataResponse"]["features"]:
        properties = feature["properties"]
        feature = Station(**properties)
        features.append(feature)
        
    return features