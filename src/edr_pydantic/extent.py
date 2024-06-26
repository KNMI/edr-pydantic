from typing import List
from typing import Optional
from typing import Union

from pydantic import AwareDatetime

from .base_model import EdrBaseModel


class Spatial(EdrBaseModel):
    bbox: List[List[float]]
    crs: str


class Temporal(EdrBaseModel):
    # TODO: Validate this list has two items (C.7.  Temporal Object)
    interval: List[List[AwareDatetime]]
    # TODO: Validate this is a list of ISO 8601 single time, ISO 8601 time duration or ISO 8601 interval
    values: List[str]
    trs: str


class Vertical(EdrBaseModel):
    interval: List[List[str]]
    values: List[str]
    vrs: str


class Custom(EdrBaseModel):
    id: str
    interval: List[List[Union[str, float]]]
    values: Optional[List[Union[str, float]]] = None
    reference: str


class Extent(EdrBaseModel):
    spatial: Spatial
    temporal: Optional[Temporal] = None
    vertical: Optional[Vertical] = None
    custom: Optional[List[Custom]] = None
