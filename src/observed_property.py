from typing import List
from typing import Optional

from .my_base_model import EDRBaseModel


class Category(EDRBaseModel):
    id: str
    label: str
    description: Optional[str] = None


class ObservedProperty(EDRBaseModel):
    id: Optional[str] = None
    label: str
    description: Optional[str] = None
    categories: Optional[List[Category]] = None
