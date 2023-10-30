from __future__ import annotations

from typing import List
from typing import Optional

from .base_model import EdrBaseModel
from .link import Link


class Provider(EdrBaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


class Contact(EdrBaseModel):
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


class LandingPageModel(EdrBaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    links: List[Link]
    keywords: Optional[List[str]] = None
    provider: Optional[Provider] = None
    contact: Optional[Contact] = None


class ConformanceModel(EdrBaseModel):
    conformsTo: List[str]  # noqa: N815
