from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict


class EDRBaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="forbid",
        str_min_length=1,
        validate_default=True,
        validate_assignment=True,
    )
