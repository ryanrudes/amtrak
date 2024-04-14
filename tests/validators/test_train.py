from utils import ensure_success, ensure_failure, ensure_field_failure

from pydantic import TypeAdapter
from datetime import datetime

from amtrak.enums import (
    Compass,
    TrainState,
)

from amtrak import Train

default_payload = {
    "ID": "1270846",
    "OBJECTID": "12",
    "CMSID": "1241245666812",
    "gx_id": "1270987",
    "ID": "1270856",
    "RouteName": "Pacific Surfliner",
    "EventCode": "None",
    "lat": "40.752455",
    "lon": "-117.1693",
    "OrigCode": "NYP",
    "DestCode": "WAS",
    "ViewStn1": "None",
    "ViewStn2": "None",
    "Velocity": "None",
    "Heading": "None",
    "TrainNum": "2162",
    "StatusMsg": "None",
    "created_at": "4/1/2024 3:31:12 PM",
    "updated_at": "4/1/2024 3:34:29 PM",
    "TrainState": "Predeparture",
    "Aliases": "None",
    "LastValTS": "4/1/2024 12:34:00 PM",
    "OriginTZ": "P",
    "OrigSchDep": "3/14/2024 7:23:00 AM",
}

ta = TypeAdapter(Train)

def test_view_station_1():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.view_station1 is None
    
    # Test None
    payload["ViewStn1"] = None
    train = Train.model_validate(payload)
    assert train.view_station1 is None
    
    # Test datetime
    payload["ViewStn1"] = "4/1/2024 3:34:35 PM"
    train = Train.model_validate(payload)
    assert train.view_station1 == datetime(2024, 4, 1, 15, 34, 35)
    
    # Test failure
    blacklist = ["none", "", "4/1/24 3:34:35 PM"]
    ensure_field_failure(blacklist, ta, payload, field = "ViewStn1")

def test_view_station_2():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.view_station2 is None
    
    # Test None
    payload["ViewStn2"] = None
    train = Train.model_validate(payload)
    assert train.view_station2 is None
    
    # Test datetime
    payload["ViewStn2"] = "4/1/2024 3:34:35 PM"
    train = Train.model_validate(payload)
    assert train.view_station2 == datetime(2024, 4, 1, 15, 34, 35)
    
    # Test failure
    blacklist = ["none", "", "4/1/24 3:34:35 PM"]
    ensure_field_failure(blacklist, ta, payload, field = "ViewStn2")

def test_velocity():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.velocity is None
    
    # Test None
    payload["Velocity"] = None
    train = Train.model_validate(payload)
    assert train.velocity is None
    
    # Test float
    payload["Velocity"] = "5.81604391336441E-02"
    train = Train.model_validate(payload)
    assert train.velocity == 5.81604391336441E-02
    
    # Test failure
    blacklist = ["none", "", "4/1/24 3:34:35 PM"]
    ensure_field_failure(blacklist, ta, payload, field = "ViewStn2")
    
def test_heading():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.heading is None
    
    # Test None
    payload["Heading"] = None
    train = Train.model_validate(payload)
    assert train.heading is None
    
    # Test cardinal direction
    payload["Heading"] = "NE"
    train = Train.model_validate(payload)
    assert train.heading == Compass.NORTHEAST
    
    # Test failure
    blacklist = ["none", "", "nurthest"]
    ensure_field_failure(blacklist, ta, payload, field = "Heading")
    
def test_status():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.status is None
    
    # Test None
    payload["StatusMsg"] = None
    train = Train.model_validate(payload)
    assert train.status is None

def test_event_code():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.event is None
    
    # Test None
    payload["EventCode"] = None
    train = Train.model_validate(payload)
    assert train.event is None
    
def test_train_state():
    payload = default_payload.copy()
    
    # Test "Predeparture"
    train = Train.model_validate(payload)
    assert train.state == TrainState.PREDEPARTURE
    
    # Test "Active"
    payload["TrainState"] = "Active"
    train = Train.model_validate(payload)
    assert train.state == TrainState.ACTIVE
    
    # Test "Completed"
    payload["TrainState"] = "Completed"
    train = Train.model_validate(payload)
    assert train.state == TrainState.COMPLETED
    
    # Test failure
    blacklist = ["none", "", "predeparture", "active", "completed"]
    ensure_field_failure(blacklist, ta, payload, field = "TrainState")

def test_aliases():
    payload = default_payload.copy()
    
    # Test "None"
    train = Train.model_validate(payload)
    assert train.aliases == []
    
    # Test None
    payload["Aliases"] = None
    train = Train.model_validate(payload)
    assert train.aliases == []
    
    # Test single alias
    payload["Aliases"] = "123"
    train = Train.model_validate(payload)
    assert train.aliases == [123]
    
    # Test multiple aliases
    payload["Aliases"] = "123,456,789"
    train = Train.model_validate(payload)
    assert train.aliases == [123, 456, 789]

def test_timezone():
    payload = default_payload.copy()
    
    # Test "P"
    train = Train.model_validate(payload)
    assert train.timezone == "America/Los_Angeles"
    
    # Test "E"
    payload["OriginTZ"] = "E"
    train = Train.model_validate(payload)
    assert train.timezone == "America/New_York"
    
    # Test "C"
    payload["OriginTZ"] = "C"
    train = Train.model_validate(payload)
    assert train.timezone == "America/Chicago"
    
    # Test "M"
    payload["OriginTZ"] = "M"
    train = Train.model_validate(payload)
    assert train.timezone == "America/Denver"