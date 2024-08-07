import os
import json


def read_transactions(file_path):
    """ Читает данные о транзакциях из JSON файла по указанному пути и возвращает список транзакций."""
    transactions = []
    if not os.path.exists(file_path):
        return transactions

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                transactions = data
        except json.JSONDecodeError:
            print("Ошибка чтения JSON файла")
    return transactions
