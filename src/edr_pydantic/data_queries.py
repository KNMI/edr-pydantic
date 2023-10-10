from typing import Optional

from .link import EDRQueryLink
from .my_base_model import EDRBaseModel


class EDRQuery(EDRBaseModel):
    link: EDRQueryLink


class DataQueries(EDRBaseModel):
    position: Optional[EDRQuery] = None
    radius: Optional[EDRQuery] = None
    area: Optional[EDRQuery] = None
    cube: Optional[EDRQuery] = None
    trajectory: Optional[EDRQuery] = None
    corridor: Optional[EDRQuery] = None
    locations: Optional[EDRQuery] = None
    items: Optional[EDRQuery] = None
    # TODO Separate Instance and Collection objects
    instances: Optional[EDRQuery] = None
