from typing import List
from typing import Optional

from pydantic import AwareDatetime

from .my_base_model import EDRBaseModel


class Spatial(EDRBaseModel):
    bbox: List[List[float]]
    crs: str


class Temporal(EDRBaseModel):
    interval: List[List[AwareDatetime]]
    values: List[str]
    trs: str


class Vertical(EDRBaseModel):
    interval: List[List[str]]
    values: List[str]
    vrs: str


class Extent(EDRBaseModel):
    spatial: Spatial
    temporal: Optional[Temporal] = None
    vertical: Optional[Vertical] = None
