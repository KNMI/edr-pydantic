from edr_pydantic.extent import IntervalLen


def test_interval_len():
    assert IntervalLen.min_length == 2, "Temporal intervals must have at least 2 items"
    assert IntervalLen.max_length == 2, "Temporal intervals must have at most 2 items"
