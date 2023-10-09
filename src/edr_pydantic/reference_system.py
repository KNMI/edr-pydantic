from .my_base_model import EDRBaseModel


# TODO req A.24 vs object CRSDetails
class CRS(EDRBaseModel):
    name: str  # MAY EPSG code
    wkt: str  # SHALL Well Known Text
