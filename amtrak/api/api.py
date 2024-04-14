from amtrak.objects import Station
from amtrak.api.endpoints.stations import get_stations
from typing import List

class API:
    def get_stations(self) -> List[Station]:
        """
        Retrieves a list of stations.

        Returns:
            A list of Feature objects representing the stations.
        """
        return get_stations()