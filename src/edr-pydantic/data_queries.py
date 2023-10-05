from typing import Optional
from typing import Union

from .my_base_model import EDRBaseModel
from .variables import CorridorVariables
from .variables import CubeVariables
from .variables import ItemVariables
from .variables import RadiusVariables
from .variables import Variables


class EDRQueryLink(EDRBaseModel):
    href: str
    rel: str
    variables: Union[Variables, CubeVariables, CorridorVariables, ItemVariables, RadiusVariables]


# TODO why not normal Link object?
class EDRQuery(EDRBaseModel):
    link: EDRQueryLink


class DataQueries(EDRBaseModel):
    position: Optional[EDRQuery] = None
    radius: Optional[EDRQuery] = None
    area: Optional[EDRQuery] = None
    cube: Optional[EDRQuery] = None
    trajectory: Optional[EDRQuery] = None
    corridor: Optional[EDRQuery] = None
    # TODO difference object/req: item, location, plus instances?
    locations: Optional[EDRQuery] = None
    items: Optional[EDRQuery] = None
