from typing import Optional
from typing import Union

from .my_base_model import EDRBaseModel
from .variables import CorridorVariables
from .variables import CubeVariables
from .variables import ItemVariables
from .variables import RadiusVariables
from .variables import Variables


class Link(EDRBaseModel):
    href: str
    rel: str
    # TODO A.21 & A.23 all links shall include rel and type? rc-collections-info-links
    type: Optional[str] = None
    hreflang: Optional[str] = None
    title: Optional[str] = None
    length: Optional[int] = None
    templated: Optional[bool] = None
    # TODO dataquery link separate because variables is required there?
    variables: Optional[Union[Variables, CubeVariables, CorridorVariables, ItemVariables, RadiusVariables]]
