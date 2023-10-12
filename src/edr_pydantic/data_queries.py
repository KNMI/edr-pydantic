from typing import Optional

from .base_model import EdrBaseModel
from .link import EDRQueryLink


class EDRQuery(EdrBaseModel):
    link: EDRQueryLink


class DataQueries(EdrBaseModel):
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
