import pytest

from home_1.src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("input_data, expected_output", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("4567890123456789", "4567 89** **** 6789"),
    ("7890123456789123", "7890 12** **** 9123"),
])
def test_get_mask_card_number(input_data: str, expected_output: str) -> None:
    assert get_mask_card_number(input_data) == expected_output


@pytest.mark.parametrize("input_data, expected_output", [
    ("73654108430135874305", "**4305"),
])
def test_get_mask_account(input_data: str, expected_output: str) -> None:
    assert get_mask_account(input_data) == expected_output
