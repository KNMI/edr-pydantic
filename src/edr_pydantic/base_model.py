from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict


class EdrBaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        str_min_length=1,
        validate_default=True,
        validate_assignment=True,
        strict=True,
    )
