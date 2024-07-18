from typing import List

import pytest


@pytest.fixture
def card_number_data() -> list[tuple[str, str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("4567890123456789", "4567 89** **** 6789"),
        ("7890123456789123", "7890 12** **** 9123"),
    ]


@pytest.fixture
def account_card_data() -> list[tuple[str, str]]:
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
    ]


@pytest.fixture
def id_data() -> List:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
