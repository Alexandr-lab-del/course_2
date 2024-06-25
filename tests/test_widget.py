import pytest

from home_2.src.widget import get_data


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    """Тест правильности работы функции mask_account_card
    на конкретных входных данных и ожидаемом выводе"""


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ],
)
def test_get_data(input_data: str, expected_output: str) -> None:
    """функция для проверки правильности работы функции get_data
    на конкретных входных данных и ожидаемом выводе"""
    assert get_data(input_data) == expected_output
