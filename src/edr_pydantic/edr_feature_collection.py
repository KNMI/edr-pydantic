from typing import Dict

from edr_pydantic.base_model import EdrBaseModel
from edr_pydantic.parameter import Parameter
from geojson_pydantic import FeatureCollection  # type: ignore


class EDRFeatureCollection(EdrBaseModel, FeatureCollection):
    parameters: Dict[str, Parameter]
