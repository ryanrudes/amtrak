# TODO: There may be more possible states

from enum import Enum

class TrainState(Enum):
    """
    Enum representing the state of a train.
    
    Attributes:
        PREDEPARTURE (str): The train is in predeparture state.
        ACTIVE (str): The train is active and running.
        COMPLETED (str): The train has completed its journey.
    """
    PREDEPARTURE = "Predeparture"
    ACTIVE = "Active"
    COMPLETED = "Completed"