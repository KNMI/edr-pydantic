from .base_model import EdrBaseModel


class CRS(EdrBaseModel):
    name: str  # # This MAY be an EPSG code
    # TODO: Implement WKT (Well Known Text) validator
    wkt: str
