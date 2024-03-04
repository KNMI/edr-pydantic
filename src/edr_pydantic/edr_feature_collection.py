from typing import Dict
from typing import Optional

from covjson_pydantic.parameter import Parameter  # type: ignore
from edr_pydantic.base_model import EdrBaseModel
from geojson_pydantic import FeatureCollection  # type: ignore


class EDRFeatureCollection(EdrBaseModel, FeatureCollection):
    parameters: Optional[Dict[str, Parameter]] = None
