import pytest
from wb_parser.services.validator import wb_query_validator
from wb_parser.config import WB_V13_MAX_QUERY_LENGTH

VALID_QUERIES = [
    "ноутбук",
    "a" * WB_V13_MAX_QUERY_LENGTH,
]

INVALID_QUERIES = [
    (None),
    (123),
    (""),
    ("a" * (WB_V13_MAX_QUERY_LENGTH + 1)),
]

@pytest.mark.parametrize("query", VALID_QUERIES)
def test_wb_query_validator_accepts_valid_queries(query):
    assert wb_query_validator(query) is None

@pytest.mark.parametrize("query", INVALID_QUERIES)
def test_wb_query_validator_rejects_invalid_queries(query):
    with pytest.raises(ValueError):
        wb_query_validator(query)