# OGC Enviromental Data Retrieval (EDR) API Pydantic

This repository contains the edr-pydantic Python package. It provides [Pydantic](https://pydantic-docs.helpmanual.io/) models
for the [OGC Enviromental Data Retrieval (EDR) API](https://ogcapi.ogc.org/edr/).
This can, for example, be used to help develop an EDR API using FastAPI.

## Install
```shell
pip install edr-pydantic
```

Or to install from source:

```shell
pip install git+https://github.com/KNMI/edr-pydantic.git
```

## Usage

```python
from edr_pydantic.collections import Collection
from edr_pydantic.data_queries import EDRQuery, EDRQueryLink
from edr_pydantic.extent import Extent, Spatial
from edr_pydantic.link import Link
from edr_pydantic.observed_property import ObservedProperty
from edr_pydantic.parameter import Parameter
from edr_pydantic.unit import Unit
from edr_pydantic.variables import Variables

c = Collection(
    id="hrly_obs",
    title="Hourly Site Specific observations",
    description="Observation data for UK observing sites",
    extent=Extent(
        spatial=Spatial(
            bbox=[
                [-15.0, 48.0, 5.0, 62.0]
            ],
            crs="WGS84"
        )
    ),
    links=[
        Link(
            href="https://example.org/uk-hourly-site-specific-observations",
            rel="service-doc"
        )
    ],
    data_queries={
        'position': EDRQuery(
            link=EDRQueryLink(
                href="https://example.org/edr/collections/hrly_obs/position?coords={coords}",
                rel="data",
                variables=Variables(
                    query_type="position",
                    output_formats=[
                        "CoverageJSON"
                    ]
                )
            )
        )
    },
    parameter_names={
        "Wind Direction": Parameter(
            unit=Unit(
                label="degree true"
            ),
            observedProperty=ObservedProperty(
                id="https://codes.wmo.int/common/quantity-kind/_windDirection",
                label="Wind Direction"
            )
        )
    }
)

print(c.model_dump_json(indent=2, exclude_none=True))
```

Will print
```json
{
  "id": "hrly_obs",
  "title": "Hourly Site Specific observations",
  "description": "Observation data for UK observing sites",
  "links": [
    {
      "href": "https://example.org/uk-hourly-site-specific-observations",
      "rel": "service-doc"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -15.0,
          48.0,
          5.0,
          62.0
        ]
      ],
      "crs": "WGS84"
    }
  },
  "data_queries": {
    "position": {
      "link": {
        "href": "https://example.org/edr/collections/hrly_obs/position?coords={coords}",
        "rel": "data",
        "variables": {
          "query_type": "position",
          "output_formats": [
            "CoverageJSON"
          ]
        }
      }
    }
  },
  "parameter_names": {
    "Wind Direction": {
      "type": "Parameter",
      "unit": {
        "label": "degree true"
      },
      "observedProperty": {
        "id": "https://codes.wmo.int/common/quantity-kind/_windDirection",
        "label": "Wind Direction"
      }
    }
  }
}
```

## Contributing

Make an editable install from within the repository root

```shell
pip install -e '.[test]'
```

### Running tests

```shell
pytest tests/
```

## Real world usage

This library is used to build an Environmental Data Retrieval (EDR) API, serving observation data from surface weather data station data from the KNMI. See the [KNMI Data Platform](https://developer.dataplatform.knmi.nl/edr-api).

## TODOs
Help is wanted in the following areas to fully implement the EDR spec:
* See TODOs in code listing various small inconsistencies in the spec
* In various places there could be more validation on content

## License

Apache License, Version 2.0
