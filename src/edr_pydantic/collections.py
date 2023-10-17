from typing import List
from typing import Optional

from .base_model import EdrBaseModel
from .data_queries import DataQueries
from .extent import Extent
from .link import Link
from .parameter import Parameters


class Collection(EdrBaseModel):
    id: str
    title: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[List[str]] = None
    links: List[Link]
    extent: Extent
    data_queries: Optional[DataQueries] = None
    # TODO According to req A.13 it shall be CRS object, according to C.1 it is a string array
    crs: Optional[List[str]] = None
    output_formats: Optional[List[str]] = None
    parameter_names: Parameters
    # TODO According to req A.13 may have distanceunits. If radius is in link, it shall have distanceunits
    distanceunits: Optional[List[str]] = None


class Collections(EdrBaseModel):
    links: List[Link]
    collections: List[Collection]


# For now, the instance metadata corresponds to the first collection metadata. So they have equal classes
class Instance(Collection):
    pass


class Instances(EdrBaseModel):
    links: List[Link]
    instances: List[Instance]
