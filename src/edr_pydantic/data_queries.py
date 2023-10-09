from typing import Optional
from typing import Union

from .my_base_model import EDRBaseModel
from .variables import CorridorVariables
from .variables import CubeVariables
from .variables import ItemVariables
from .variables import RadiusVariables
from .variables import Variables


class EDRQueryLink(EDRBaseModel, extra="allow"):
    href: str
    rel: str
    variables: Union[Variables, CubeVariables, CorridorVariables, ItemVariables, RadiusVariables]


# TODO Why not use the Link object, difference is required variables for this link?
class EDRQuery(EDRBaseModel):
    link: EDRQueryLink


class DataQueries(EDRBaseModel):
    position: Optional[EDRQuery] = None
    radius: Optional[EDRQuery] = None
    area: Optional[EDRQuery] = None
    cube: Optional[EDRQuery] = None
    trajectory: Optional[EDRQuery] = None
    corridor: Optional[EDRQuery] = None
    # TODO Difference object/req: item, location, plus instances (only for collection)?
    locations: Optional[EDRQuery] = None
    items: Optional[EDRQuery] = None
    instances: Optional[EDRQuery] = None
