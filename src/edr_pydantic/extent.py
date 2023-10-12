from typing import List
from typing import Optional

from pydantic import AwareDatetime

from .base_model import EdrBaseModel


class Spatial(EdrBaseModel):
    bbox: List[List[float]]
    crs: str


class Temporal(EdrBaseModel):
    interval: List[List[AwareDatetime]]
    values: List[str]
    trs: str


class Vertical(EdrBaseModel):
    interval: List[List[str]]
    values: List[str]
    vrs: str


class Extent(EdrBaseModel):
    spatial: Spatial
    temporal: Optional[Temporal] = None
    vertical: Optional[Vertical] = None
