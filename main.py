from src.file_operations import read_transactions
from src.currency_converter import convert_to_rubles


def main():
    """читает транзакции из JSON файла,
    конвертирует их в рубли"""
    transactions = read_transactions('data/operations.json')
    if not transactions:
        print("Нет данных для обработки.")
        return

    for transaction in transactions:
        operation_amount = transaction.get('operationAmount', {})
        currency = operation_amount.get('currency', {}).get('code')
        amount = operation_amount.get('amount')

        if currency and amount is not None:
            amount_in_rubles = convert_to_rubles(currency, amount)
            if amount_in_rubles is not None:
                print(f"Сумма транзакции в рублях: {amount_in_rubles}")
            else:
                print(f"Не удалось конвертировать валюту {currency} для суммы {amount}")
        else:
            print("Некорректные данные транзакции")


if __name__ == "__main__":
    main()
