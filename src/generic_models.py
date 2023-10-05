from typing import List

from covjson_pydantic.domain import DomainType

from .my_base_model import EDRBaseModel


# TODO Cannot find in the spec? Checken of ie gebruikt wordt in backends edr
class SupportedQueries(EDRBaseModel):
    model_config = {
        "json_schema_extra": {
            "domain_types": {
                "description": "A list of domain types from which can be determined what endpoints are allowed."
            },
            "has_location": {
                "description": "A boolean from which can be determined if the backend has the /locations endpoint."
            },
            "examples": [
                {
                    "domain_types": "When [DomainType.point_series] is returned, "
                    "the /position endpoint is allowed but /cube is not allowed.",
                    "has_locations": "When True is returned, the backend has the /locations endpoint.",
                }
            ],
        }
    }
    domain_types: List[DomainType]
    has_locations: bool
