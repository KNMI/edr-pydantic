from typing import Optional
from typing import Union

from pydantic import model_validator

from .base_model import EdrBaseModel


class Symbol(EdrBaseModel, extra="allow"):
    value: str
    type: str


class Unit(EdrBaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    symbol: Optional[Union[str, Symbol]] = None

    @model_validator(mode="after")
    def check_either_label_or_symbol(self):
        if self.label is None and self.symbol is None:
            raise ValueError("Either 'label' or 'symbol' should be set")

        return self
