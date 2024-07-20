from src.utils import read_transactions
from src.external_api import convert_to_rubles_json


def main():
    """Основная функция программы. Считывает файл с транзакциями и конвертирует сумму в рубли."""
    file_path = input("Введите путь к файлу (JSON, CSV, Excel): ")

    if file_path.endswith('.json'):
        transactions = read_transactions(file_path)
        if not transactions:
            print("Нет данных для обработки.")
            return

        for transaction in transactions:
            operation_amount = transaction.get('operationAmount', {})
            currency = operation_amount.get('currency', {}).get('code')
            amount = operation_amount.get('amount')

            if currency and amount is not None:
                amount_in_rubles = convert_to_rubles_json(currency, amount)
                if amount_in_rubles is not None:
                    print(f"Сумма транзакции в рублях: {amount_in_rubles}")
                else:
                    print(f"Не удалось конвертировать валюту {currency} для суммы {amount}")
            else:
                print("Некорректные данные транзакции")

    elif file_path.endswith('.csv'):
        transactions = read_transactions(file_path)
        if not transactions:
            print("Нет данных для обработки.")
            return

        for transaction in transactions:
            currency = transaction.get('currency')
            amount = transaction.get('amount')

            if currency and amount is not None:
                amount_in_rubles = convert_to_rubles_json(currency, amount)
                if amount_in_rubles is not None:
                    print(f"Сумма транзакции в рублях: {amount_in_rubles}")
                else:
                    print(f"Не удалось конвертировать валюту {currency} для суммы {amount}")
            else:
                print("Некорректные данные транзакции")

    elif file_path.endswith('.xlsx'):
        transactions = read_transactions(file_path)
        if not transactions:
            print("Нет данных для обработки.")
            return

        for transaction in transactions:
            currency = transaction.get('currency')
            amount = transaction.get('amount')

            if currency and amount is not None:
                amount_in_rubles = convert_to_rubles_json(currency, amount)
                if amount_in_rubles is not None:
                    print(f"Сумма транзакции в рублях: {amount_in_rubles}")
                else:
                    print(f"Не удалось конвертировать валюту {currency} для суммы {amount}")
            else:
                print("Некорректные данные транзакции")

    else:
        print("Формат файла не поддерживается.")


if __name__ == "__main__":
    main()
