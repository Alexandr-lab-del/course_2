from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    """Тестируем функцию filter_by_currency"""
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1", "id": 1},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2", "id": 2},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3", "id": 3},
    ]
    currency = "USD"

    filtered = filter_by_currency(transactions, currency)
    result_ids = [transaction["id"] for transaction in filtered]

    assert result_ids == [1, 3]


def test_transaction_descriptions():
    """Тестируем функцию transaction_descriptions"""
    transactions = [
        {"description": "Description 1"},
        {"description": "Description 2"},
        {"description": "Description 3"},
    ]

    descriptions = transaction_descriptions(transactions)
    result_desc = [desc for desc in descriptions]

    assert result_desc == ["Description 1", "Description 2", "Description 3"]


def test_card_number_generator():
    """Тестируем функцию card_number_generator"""
    card_numbers = card_number_generator(1000, 1002)
    result_card_numbers = [card for card in card_numbers]

    assert len(result_card_numbers) == 3
    assert all(len(card) == 16 for card in result_card_numbers)


if __name__ == "__main__":
    test_filter_by_currency()
    test_transaction_descriptions()
    test_card_number_generator()
