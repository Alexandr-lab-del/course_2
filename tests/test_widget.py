import pytest

from src.widget import get_data, mask_account_card


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
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-11T", "11.07.2019"),
        ("2017-07-11T02:26:18.671407", "11.07.2017"),
        ("2016-07-11T02:26:18.671407", "11.07.2016"),
    ],
)
def test_get_data(input_data: str, expected_output: str) -> None:
    """функция для проверки правильности работы функции get_data
    на конкретных входных данных и ожидаемом выводе"""
    assert get_data(input_data) == expected_output


def test_get_data_error():
    with pytest.raises(ValueError) as exc_info:
        get_data(" ")
        assert str(exc_info.value) == "Ошибка, введите значение"
