from .my_base_model import EDRBaseModel


# TODO req A.24 unclear whether property is called name or crs?
class CRSDetails(EDRBaseModel):
    crs: str  # MAY EPSG code
    wkt: str  # SHALL Well Known Text
