import pytest
from wb_parser.services.validator.wb import wb_id_validator

VALID_IDS = [
    12345678,
    123456789,
    1234567890,
    12345678900
]

INVALID_IDS = [
    (None),
    ("123"),
    (-1),
    (123)
]

@pytest.mark.parametrize("wb_id", VALID_IDS)
def test_wb_id_validator_accepts_valid_ids(wb_id):
    assert wb_id_validator(wb_id) is None

@pytest.mark.parametrize("wb_id", INVALID_IDS)
def test_wb_id_validator_rejects_invalid_ids(wb_id):
    with pytest.raises(ValueError):
        wb_id_validator(wb_id)