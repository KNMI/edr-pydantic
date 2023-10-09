from typing import List
from typing import Optional

from pydantic import AwareDatetime

from .my_base_model import EDRBaseModel


class Spatial(EDRBaseModel):
    bbox: List[List[float]]
    crs: str


class Temporal(EDRBaseModel):
    # TODO Check: Array of ISO 8601 Data Array
    interval: List[List[AwareDatetime]]
    # TODO Check: ISO 8601 Data Array
    values: List[str]
    trs: str


class Vertical(EDRBaseModel):
    interval: List[List[float]]
    values: List[float]
    vrs: str


class Extent(EDRBaseModel):
    spatial: Spatial
    temporal: Optional[Temporal] = None
    vertical: Optional[Vertical] = None
