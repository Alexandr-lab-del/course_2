from typing import Dict, Iterator, List, Union


def filter_by_currency(
    transactions: List[Dict[str, Union[str, Dict[str, Union[str, str]]]]], currency: str
) -> Iterator[Dict[str, Union[str, Dict[str, Union[str, str]]]]]:
    """Фильтрует транзакции по валюте"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount")
        if isinstance(operation_amount, dict):
            currency_info = operation_amount.get("currency")
            if isinstance(currency_info, dict) and currency_info.get("code") == currency:
                yield transaction


def transaction_descriptions(transactions: List[Dict[str, str]]) -> Iterator[str]:
    """Извлекает описания из транзакций"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start_num: int, end_num: int) -> Iterator[int]:
    """Генерирует номера карт"""
    for number in range(start_num, end_num + 1):
        yield f"{number:016d}"
