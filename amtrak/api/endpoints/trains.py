import requests

def get_trains():
    endpoint = "https://maps.amtrak.com/services/MapDataService/trains/getTrainsData"
    response = requests.get(endpoint)
    text = response.text
    