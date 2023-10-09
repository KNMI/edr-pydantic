from typing import Dict
from typing import List
from typing import Optional

from .data_queries import DataQueries
from .extent import Extent
from .link import Link
from .my_base_model import EDRBaseModel
from .parameter import Parameter


class Collection(EDRBaseModel):
    id: str
    title: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[List[str]] = None
    links: List[Link]
    extent: Extent
    data_queries: Optional[DataQueries] = None
    # TODO According to req A.13 it should be CRSDetails object
    crs: Optional[List[str]] = None
    output_formats: Optional[List[str]] = None
    parameter_names: Dict[str, Parameter]
    # TODO According to req A.13 MAY have distanceunits. If radius is in link, it SHALL have distanceunits
    distanceunits: Optional[List[str]] = None


class Collections(EDRBaseModel):
    links: List[Link]
    collections: List[Collection]


# For now, the instance metadata corresponds to the first collection metadata. So they have equal classes
class Instance(Collection):
    pass


class Instances(EDRBaseModel):
    links: List[Link]
    instances: List[Instance]
