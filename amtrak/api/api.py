from amtrak.validators import Feature
from amtrak.api.endpoints.stations import get_stations
from typing import List

class API:
    def get_stations(self) -> List[Feature]:
        """
        Retrieves a list of stations.

        Returns:
            A list of Feature objects representing the stations.
        """
        return get_stations()