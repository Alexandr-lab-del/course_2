import pytest

from typing import List, Dict

from home_3.processing import filter_by_state, sort_by_date


@pytest.fixture
def input_data() -> List:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize("target_state: str, expected_output: int", [("EXECUTED", 2), ("CANCELED", 2)])
def test_filter_by_state(input_data: List[Dict[str, str]], target_state: str, expected_output: int) -> None:
    """функция для проверки правильности работы функции filter_by_state
        на конкретных входных данных и ожидаемом выводе"""
    result = filter_by_state(input_data, target_state)
    assert len(result) == expected_output
    for item in result:
        assert item["state"] == target_state


@pytest.mark.parametrize("reverse: bool, expected_result: List[Dict[str, str]]", [
    (True, [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]),
    (False, [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]),
])
def test_sort_by_date(input_data: List[Dict[str, str]], reverse: bool, expected_result: List[Dict[str, str]]) -> None:
    """функция для проверки правильности работы функции sort_by_date
        на конкретных входных данных и ожидаемом выводе"""
    result = sort_by_date(input_data, reverse)
    assert result == expected_result
