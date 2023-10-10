from .my_base_model import EDRBaseModel


class CRS(EDRBaseModel):
    name: str  # MAY EPSG code
    wkt: str  # SHALL Well Known Text
