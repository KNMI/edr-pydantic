import json
from pathlib import Path

import pytest
from edr_pydantic.capabilities import LandingPageModel
from edr_pydantic.collections import Collections
from edr_pydantic.collections import Instance
from edr_pydantic.extent import Extent
from edr_pydantic.extent import Temporal
from edr_pydantic.observed_property import ObservedProperty
from edr_pydantic.parameter import Parameter
from edr_pydantic.parameter import Parameters
from edr_pydantic.unit import Unit
from pydantic import ValidationError

happy_cases = [
    ("knmi-example-collections.json", Collections),
    ("doc-example-collections.json", Collections),
    ("simple-instance.json", Instance),
    ("landing-page.json", LandingPageModel),
    ("doc-example-extent.json", Extent),
    ("parameter-names.json", Parameters),
    ("parameter-with-data-type.json", Parameters),
    ("parameter-with-extent.json", Parameter),
]


@pytest.mark.parametrize("file_name, object_type", happy_cases)
def test_happy_cases(file_name, object_type):
    file = Path(__file__).parent.resolve() / "test_data" / file_name
    # Put JSON in default unindented format
    with open(file, "r") as f:
        data = json.load(f)
    json_string = json.dumps(data, separators=(",", ":"), ensure_ascii=False)

    # Round-trip
    assert object_type.model_validate_json(json_string).model_dump_json(exclude_none=True, by_alias=True) == json_string


error_cases = [
    ("label-or-symbol-unit.json", Unit, r"Either 'label' or 'symbol' should be set"),
    ("temporal-interval-length1.json", Temporal, r"List should have at least 2 items after validation"),
    ("temporal-interval-length3.json", Temporal, r"List should have at most 2 items after validation, not 3"),
    ("parameter-invalid-data-type.json", Parameter, r"Input should be 'integer', 'float' or 'string'"),
]


@pytest.mark.parametrize("file_name, object_type, error_message", error_cases)
def test_error_cases(file_name, object_type, error_message):
    file = Path(__file__).parent.resolve() / "test_data" / file_name
    # Put JSON in default unindented format
    with open(file, "r") as f:
        data = json.load(f)
    json_string = json.dumps(data, separators=(",", ":"))

    with pytest.raises(ValidationError, match=error_message):
        object_type.model_validate_json(json_string)


def test_data_type_alias():
    p = Parameter(observedProperty=ObservedProperty(label="Wind"), dataType="integer")

    # This tests for the current observed Pydantic behavior with model_dump() and the `by_alias` setting
    assert (
        p.model_dump_json(exclude_none=True)
        == '{"type":"Parameter","dataType":"integer","observedProperty":{"label":"Wind"}}'
    )
    assert (
        p.model_dump_json(exclude_none=True, by_alias=True)
        == '{"type":"Parameter","data-type":"integer","observedProperty":{"label":"Wind"}}'
    )
