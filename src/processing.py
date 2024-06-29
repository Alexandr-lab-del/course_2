def filter_by_state(data: list, target_state: str = "EXECUTED") -> list:
    """Функция фильтрации операций по ключу state"""
    sorted_result = []
    for index in data:
        if index.get("state", "EXECUTED") == target_state:
            sorted_result.append(index)
    return sorted_result


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

result_default = filter_by_state(input_data)
print(result_default)

result_canceled = filter_by_state(input_data, "CANCELED")
print(result_canceled)


def sort_by_date(data: list, reverse: bool = False) -> list:
    """Функция сортирует список словарей по дате в порядке убывания или возрастания"""
    data_sort = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return data_sort


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

"Сортировка списка по дате по убыванию"
sorted_data_decreasing = sort_by_date(input_data, reverse=True)
print("Сортировка по убыванию")
for index in sorted_data_decreasing:
    print(index)

"Сортировка списка по дате по возрастания"
sorted_data_increasing = sort_by_date(input_data, reverse=False)
print("Сортировка по возрастанию")
for index in sorted_data_increasing:
    print(index)
