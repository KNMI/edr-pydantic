from typing import Dict

from covjson_pydantic.parameter import Parameter  # type: ignore
from edr_pydantic.base_model import EdrBaseModel
from geojson_pydantic import FeatureCollection  # type: ignore


class EDRFeatureCollection(EdrBaseModel, FeatureCollection):
    parameters: Dict[str, Parameter]
