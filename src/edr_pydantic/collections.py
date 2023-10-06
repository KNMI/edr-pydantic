from __future__ import annotations

from typing import List
from typing import Optional

from .data_queries import DataQueries
from .extent import Extent
from .link import Link
from .my_base_model import EDRBaseModel
from .parameter import ParameterNames


# TODO instances or collections as base?
class Collection(EDRBaseModel):
    links: List[Link]
    id: str
    extent: Extent
    parameter_names: ParameterNames
    title: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[List[str]] = None
    data_queries: Optional[DataQueries] = None
    # TODO required according to A.13, string array or crs object?
    crs: Optional[List[str]] = None
    # TODO in req as f?
    output_formats: Optional[List[str]] = None
    # TODO may have distanceunits, if radius is in link, it shall have distanceunits
    distanceunits: Optional[List[str]] = None


class CollectionsModel(EDRBaseModel):
    links: List[Link]
    collections: List[Collection]


class InstancesModel(EDRBaseModel):
    links: List[Link]
    instances: List[Instance]


# For now, the instance metadata corresponds to the first collection metadata. So they have equal classes
class Instance(Collection):
    pass
