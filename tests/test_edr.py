import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from src.edr_pydantic.collections import CollectionsModel


happy_cases = [
    ("knmi-example-collection.json", CollectionsModel),
    ("doc-example-collection.json", CollectionsModel),
]


@pytest.mark.parametrize("file_name, object_type", happy_cases)
def test_happy_cases(file_name, object_type):
    file = Path(__file__).parent.resolve() / "test_data" / file_name
    # Put JSON in default unindented format
    with open(file, "r") as f:
        data = json.load(f)
    json_string = json.dumps(data, separators=(",", ":"), ensure_ascii=False)

    # # Writing to sample.json
    # with open("sample1.json", "w") as outfile:
    #     outfile.write(json_string)
    #     # Writing to sample.json
    # with open("sample2.json", "w") as outfile:
    #     outfile.write(object_type.model_validate_json(json_string).model_dump_json(exclude_none=True))

    # Round-trip
    assert object_type.model_validate_json(json_string).model_dump_json(exclude_none=True) == json_string


error_cases = []


@pytest.mark.parametrize("file_name, object_type, error_message", error_cases)
def test_error_cases(file_name, object_type, error_message):
    file = Path(__file__).parent.resolve() / "test_data" / file_name
    # Put JSON in default unindented format
    with open(file, "r") as f:
        data = json.load(f)
    json_string = json.dumps(data, separators=(",", ":"))

    with pytest.raises(ValidationError, match=error_message):
        object_type.model_validate_json(json_string)
