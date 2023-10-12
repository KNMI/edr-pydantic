from typing import List
from typing import Optional

from .base_model import EdrBaseModel


class Variables(EdrBaseModel, extra="allow"):
    # TODO query_type required? Not according to C.3
    query_type: str
    output_formats: Optional[List[str]] = None
    # TODO If a default_output_format property exists the defined value MUST be a value contained either in the
    #  output_formats defined in the variables section or in the parent collection output_formats.
    default_output_format: Optional[str] = None


class CubeVariables(Variables):
    height_units: List[str]


class RadiusVariables(Variables):
    within_units: List[str]


class CorridorVariables(Variables):
    height_units: List[str]
    within_units: List[str]


class ItemVariables(Variables):
    # TODO: Is unclear what is meant with Requirement A.20 statement A
    pass
