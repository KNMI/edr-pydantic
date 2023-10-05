from typing import List
from typing import Optional

from pydantic import AwareDatetime

from .my_base_model import EDRBaseModel
from .reference_system import CRSDetails


class Spatial(EDRBaseModel):
    bbox: List[List[float]]
    # TODO CRS/CRSDetails/CRSOptions/str?
    crs: CRSDetails
    # TODO not in spec
    name: Optional[str] = None


class Temporal(EDRBaseModel):
    # TODO  Array of ISO 8601 Data Array
    # TODO: An array of ISO 8601 Date Array, each ISO 8601 Date Array should contain two values first being
    #  the minimum date time and second the maximum date time for information in the collection
    interval: List[List[AwareDatetime]]
    # TODO An array of ISO 8601 datestrings which details the time intervals available in the collection,
    #  each member of the array can either be a single time, an ISO 8601 time interval or an ISO 8601 time duration
    values: List[AwareDatetime]
    trs: str
    # TODO remove name not in spec
    name: Optional[str] = None


class Vertical(EDRBaseModel):
    interval: List[List[float]]
    values: List[float]
    # TODO WKT standard str
    vrs: str
    # TODO no name in spec
    name: Optional[str] = None


class Extent(EDRBaseModel):
    spatial: Spatial
    temporal: Optional[Temporal] = None
    vertical: Optional[Vertical] = None
