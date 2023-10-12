import json
from pathlib import Path

import pytest
from edr_pydantic.capabilities import LandingPageModel
from edr_pydantic.collections import Collections
from edr_pydantic.collections import Instance
from edr_pydantic.unit import Unit
from pydantic import ValidationError

happy_cases = [
    ("knmi-example-collections.json", Collections),
    ("doc-example-collections.json", Collections),
    ("simple-instance.json", Instance),
    ("landing-page.json", LandingPageModel),
]


@pytest.mark.parametrize("file_name, object_type", happy_cases)
def test_happy_cases(file_name, object_type):
    file = Path(__file__).parent.resolve() / "test_data" / file_name
    # Put JSON in default unindented format
    with open(file, "r") as f:
        data = json.load(f)
    json_string = json.dumps(data, separators=(",", ":"), ensure_ascii=False)

    # Round-trip
    assert object_type.model_validate_json(json_string).model_dump_json(exclude_none=True) == json_string


error_cases = [("label-or-symbol-unit.json", Unit, r"Either 'label' or 'symbol' should be set")]


@pytest.mark.parametrize("file_name, object_type, error_message", error_cases)
def test_error_cases(file_name, object_type, error_message):
    file = Path(__file__).parent.resolve() / "test_data" / file_name
    # Put JSON in default unindented format
    with open(file, "r") as f:
        data = json.load(f)
    json_string = json.dumps(data, separators=(",", ":"))

    with pytest.raises(ValidationError, match=error_message):
        object_type.model_validate_json(json_string)
