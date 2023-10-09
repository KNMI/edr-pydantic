from __future__ import annotations

from typing import List
from typing import Optional

from .link import Link
from .my_base_model import EDRBaseModel


class Provider(EDRBaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


class Contact(EDRBaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    hours: Optional[str] = None
    instructions: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None  # noqa: N815
    city: Optional[str] = None
    stateorprovince: Optional[str] = None
    country: Optional[str] = None


class LandingPageModel(EDRBaseModel):
    links: List[Link]
    title: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[List[str]] = None
    provider: Optional[Provider] = None
    contact: Optional[Contact] = None


class ConformanceModel(EDRBaseModel):
    conformsTo: List[str]  # noqa: N815
