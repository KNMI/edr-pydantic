from .base_model import EdrBaseModel


# TODO According to req A.13 a collection has a CRS object, according to C.1 it is a string array
# For now, this is unused
class CRS(EdrBaseModel):
    name: str  # This MAY be an EPSG code
    # TODO: Implement WKT (Well Known Text) validator
    wkt: str
