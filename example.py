from edr_pydantic.collections import Collection
from edr_pydantic.data_queries import EDRQuery
from edr_pydantic.data_queries import EDRQueryLink
from edr_pydantic.extent import Extent
from edr_pydantic.extent import Spatial
from edr_pydantic.link import Link
from edr_pydantic.observed_property import ObservedProperty
from edr_pydantic.parameter import Parameter
from edr_pydantic.unit import Unit
from edr_pydantic.variables import Variables

c = Collection(
    id="hrly_obs",
    title="Hourly Site Specific observations",
    description="Observation data for UK observing sites",
    extent=Extent(spatial=Spatial(bbox=[[-15.0, 48.0, 5.0, 62.0]], crs="WGS84")),
    links=[Link(href="https://example.org/uk-hourly-site-specific-observations", rel="service-doc")],
    data_queries={
        "position": EDRQuery(
            link=EDRQueryLink(
                href="https://example.org/edr/collections/hrly_obs/position?coords={coords}",
                rel="data",
                variables=Variables(query_type="position", output_formats=["CoverageJSON"]),
            )
        )
    },
    parameter_names={
        "Wind Direction": Parameter(
            unit=Unit(label="degree true"),
            observedProperty=ObservedProperty(
                id="https://codes.wmo.int/common/quantity-kind/_windDirection", label="Wind Direction"
            ),
        )
    },
)

print(c.model_dump_json(indent=2, exclude_none=True))
