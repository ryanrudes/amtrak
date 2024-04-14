from amtrak.api.crypto import parse
from amtrak.objects import Train

from typing import List

import requests

def get_trains(fetch = requests.get, crypto_parse = parse) -> List[Train]:
    endpoint = "https://maps.amtrak.com/services/MapDataService/trains/getTrainsData"
    response = fetch(endpoint)
    
    # Decrypt the trains
    results = crypto_parse(response.text)["features"]
    
    # Validate the trains
    trains = []
    
    for result in results:
        lon, lat = result["geometry"]["coordinates"]
        assert lon is not None and lat is not None
        properties = result["properties"]
        properties["lat"] = lat
        properties["lon"] = lon
        train = Train(**properties)
        trains.append(train)
    
    return trains