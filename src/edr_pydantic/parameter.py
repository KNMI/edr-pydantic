from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from pydantic import Field
from pydantic import model_validator
from pydantic import RootModel

from .base_model import EdrBaseModel
from .extent import Extent
from .observed_property import ObservedProperty
from .unit import Unit


class MeasurementType(EdrBaseModel):
    method: str
    # TODO: Add validation of ISO 8601 duration (including leading minus sign)
    duration: str


class Parameter(EdrBaseModel, extra="allow"):
    type: Literal["Parameter"] = "Parameter"
    id: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    dataType: Optional[Literal["integer", "float", "string"]] = Field(None, alias="data-type")  # noqa: N815
    unit: Optional[Unit] = None
    observedProperty: ObservedProperty  # noqa: N815
    extent: Optional[Extent] = None
    measurementType: Optional[MeasurementType] = None  # noqa: N815

    @model_validator(mode="after")
    def must_not_have_unit_if_observed_property_has_categories(self):
        if self.unit is not None and self.observedProperty is not None and self.observedProperty.categories is not None:
            raise ValueError(
                "A parameter object MUST NOT have a 'unit' member "
                "if the 'observedProperty' member has a 'categories' member."
            )

        return self


class Parameters(RootModel):
    root: Dict[str, Parameter]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, key):
        return self.root[key]

    def get(self, key, default=None):
        return self.root.get(key, default)


class ParameterGroup(EdrBaseModel, extra="allow"):
    type: Literal["ParameterGroup"] = "ParameterGroup"
    id: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    observedProperty: Optional[ObservedProperty] = None  # noqa: N815
    members: List[str]

    @model_validator(mode="after")
    def must_have_label_and_or_observed_property(self):
        if self.label is None and self.observedProperty is None:
            raise ValueError(
                "A parameter group object MUST have either or both the members 'label' or/and 'observedProperty'"
            )
        return self
