from pydantic import BaseModel, Field, AliasChoices, validator

from amtrak.enums import StationType

from typing import Optional, Union
from datetime import datetime

# TODO: Figure out whether we should move this file to a more approperiate directory

# TODO: Figure out whether to allow aliases of properties like:
#  * station_aliases <=> aliases
#  * station_rank <=> rank
#  * etc.
#
#  This will make the code more readable and easier to understand.
#  The downside is that it will make the code more verbose.
class Feature(BaseModel):
    object_id: int = Field(validation_alias = AliasChoices("object_id", "OBJECTID"))
    longitude: float = Field(ge = -180, le = 180, validation_alias = AliasChoices("longitude", "lon"))
    latitude: float = Field(ge = -90, le = 90, validation_alias = AliasChoices("latitude", "lat"))
    is_train_station: bool = Field(validation_alias = AliasChoices("is_train_station", "IsTrainSt"))
    zoom: int = Field(validation_alias = AliasChoices("zoom", "MapZmLvl"))
    gx_id: str = Field(min_length = 3, max_length = 3, pattern = r"^[A-Z]{3}$")
    date_modified: datetime = Field(validation_alias = AliasChoices("date_modified", "DateModif"))
    station_type: StationType = Field(validation_alias = AliasChoices("station_type", "StaType"))
    zip_code: str = Field(pattern = r"^\d{5}$|[A-Z]\d[A-Z]\s\d[A-Z]\d$", validation_alias = AliasChoices("zip_code", "Zipcode"))
    state: str = Field(min_length = 2, max_length = 2, pattern = "^[A-Z]{2}$", validation_alias = AliasChoices("state", "State"))
    city: str = Field(validation_alias = AliasChoices("city", "City"))
    address1: str = Field(validation_alias = AliasChoices("address1", "Address1"))
    address2: str = Field(validation_alias = AliasChoices("address2", "Address2"))
    name: Optional[str] = Field(validation_alias = AliasChoices("name", "Name"))
    code: str = Field(min_length = 3, max_length = 3, pattern = "^[A-Z]{3}$", validation_alias = AliasChoices("code", "Code"))
    created_at: datetime
    updated_at: datetime
    station_name: str = Field(validation_alias = AliasChoices("station_name", "StationName"))
    station_facility_name: Optional[str] = Field(validation_alias = AliasChoices("station_facility_name", "StationFacilityName"))
    station_aliases: list[str] = Field(validation_alias = AliasChoices("station_aliases", "StationAliases"))
    station_rank: Optional[int] = Field(validation_alias = AliasChoices("station_rank", "StationRank"))

    @property
    def lon(self) -> float:
        """Alias for longitude"""
        return self.longitude
    
    @property
    def lat(self) -> float:
        """Alias for latitude"""
        return self.latitude
    
    @validator("name", "station_facility_name")
    def empty_string_to_none(cls, v: Union[str, Optional[str]]) -> Optional[str]:
        if v == '' or v is None:
            return None
        return v

    @validator("station_rank", pre=True)
    def empty_int_to_none(cls, v: Union[str, Optional[int]]) -> Optional[int]:
        if v is None or v == '':
            return None
        return int(v)

    @validator("created_at", "updated_at", pre=True)
    def parse_datetime(cls, dt: Union[str, datetime]) -> datetime:
        if isinstance(dt, datetime):
            return dt
        elif isinstance(dt, str):
            return datetime.strptime(dt, "%m/%d/%Y %I:%M:%S %p")
        else:
            raise TypeError("datetime st be a string or datetime object")
    
    @validator("station_aliases", pre=True)
    def split_comma_separated(cls, v: Union[str, list[str]]) -> list[str]:
        if isinstance(v, list):
            return v
        elif isinstance(v, str):
            return [] if v == '' else v.split(',')
        else:
            raise TypeError("station_aliases must be a string or list of strings")