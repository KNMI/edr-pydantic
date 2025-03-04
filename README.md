# OGC Environmental Data Retrieval (EDR) API Pydantic

<p>
  <a href="https://github.com/knmi/edr-pydantic/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/knmi/edr-pydantic/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/knmi/edr-pydantic" target="_blank">
      <img src="https://codecov.io/gh/knmi/edr-pydantic/branch/master/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/edr-pydantic" target="_blank">
      <img src="https://img.shields.io/pypi/v/edr-pydantic?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypistats.org/packages/edr-pydantic" target="_blank">
      <img src="https://img.shields.io/pypi/dm/edr-pydantic.svg" alt="Downloads">
  </a>
  <a href="https://github.com/knmi/edr-pydantic/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/knmi/edr-pydantic.svg" alt="License">
  </a>
</p>


This repository contains the edr-pydantic Python package. It provides [Pydantic](https://pydantic-docs.helpmanual.io/) models
for the [OGC Environmental Data Retrieval (EDR) API](https://ogcapi.ogc.org/edr/).
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
from edr_pydantic.data_queries import EDRQuery, EDRQueryLink, DataQueries
from edr_pydantic.extent import Extent, Spatial
from edr_pydantic.link import Link
from edr_pydantic.observed_property import ObservedProperty
from edr_pydantic.parameter import Parameters, Parameter
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
    data_queries=DataQueries(
        position=EDRQuery(
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
    ),
    parameter_names=Parameters({
        "Wind Direction": Parameter(
            unit=Unit(
                label="degree true"
            ),
            observedProperty=ObservedProperty(
                id="https://codes.wmo.int/common/quantity-kind/_windDirection",
                label="Wind Direction"
            ),
            dataType="integer"
        )
    })
)

print(c.model_dump_json(indent=2, exclude_none=True, by_alias=True))
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
      "data-type": "integer",
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

**IMPORTANT**: The arguments `by_alias=True` to `model_dump_json()` or `model_dump()` is required to get the output as shown above. Without `by_alias=True` the attribute `data-type` will be wrongly outputted as `dataType`. This is due an issue in the [EDR spec](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/issues/605) and [Pydantic](https://github.com/pydantic/pydantic/issues/8379).


## Contributing

Make an editable install from within the repository root

```shell
pip install -e '.[test]'
```

### Running tests

```shell
pytest tests/
```

### Linting and typing

Linting and typing (mypy) is done using [pre-commit](https://pre-commit.com) hooks.

```shell
pip install pre-commit
pre-commit install
pre-commit run
```

## Related packages

* [CoverageJSON Pydantic](https://github.com/KNMI/covjson-pydantic)
* [geojson-pydantic](https://github.com/developmentseed/geojson-pydantic)

## Real world usage

This library is used to build an OGC Environmental Data Retrieval (EDR) API, serving automatic weather data station data from The Royal Netherlands Meteorological Institute (KNMI). See the [KNMI Data Platform EDR API](https://developer.dataplatform.knmi.nl/edr-api).

## TODOs
Help is wanted in the following areas to fully implement the EDR spec:
* See TODOs in code listing various small inconsistencies in the spec
* In various places there could be more validation on content

## License

Apache License, Version 2.0
