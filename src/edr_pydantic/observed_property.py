from typing import List
from typing import Optional

from .base_model import EdrBaseModel


class Category(EdrBaseModel):
    id: str
    label: str
    description: Optional[str] = None


class ObservedProperty(EdrBaseModel):
    id: Optional[str] = None
    label: str
    description: Optional[str] = None
    categories: Optional[List[Category]] = None
