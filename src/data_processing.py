import pandas as pd
import json
import collections
import re
from datetime import datetime


def process_json_data(file_path):
    """Функция для обработки данных из файла JSON"""
    converted_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            operation_amount = item.get('operationAmount', {})
            if isinstance(operation_amount, str):
                operation_amount = json.loads(operation_amount)

            currency_code = operation_amount.get('currency', {}).get('code')
            amount = operation_amount.get('amount')

            if currency_code and amount is not None:
                transaction_data = {
                    'id': item.get('id'),
                    'state': item.get('state'),
                    'date': datetime.strptime(item.get('date').split('T')[0], '%Y-%m-%d').strftime('%d.%m.%Y'),
                    'amount': amount,
                    'currency': currency_code,
                    'description': item.get('description'),
                    'from': item.get('from'),
                    'to': item.get('to')
                }
                converted_data.append(transaction_data)

    return converted_data


def process_csv_data(file_path):
    """Функция для обработки данных из файла CSV"""
    converted_data = []
    data = pd.read_csv(file_path, sep=';')

    for index, row in data.iterrows():
        date_value = row['date']
        if pd.isnull(date_value):
            continue

        if isinstance(date_value, float):
            date_str = str(date_value)
            date = datetime.fromtimestamp(float(date_str)).strftime('%d.%m.%Y')
        else:
            date = datetime.strptime(date_value.split('T')[0], '%Y-%m-%d').strftime('%d.%m.%Y')

        converted_data.append({
            'id': row['id'],
            'state': row['state'],
            'date': date,
            'amount': row['amount'],
            'currency': row['currency'],
            'description': row['description'],
            'from': row['from'],
            'to': row['to']
        })

    return converted_data


def process_excel_data(file_path):
    """Функция для обработки данных из файла Excel"""
    converted_data = []
    data = pd.read_excel(file_path)

    for index, row in data.iterrows():
        if not pd.isnull(row['date']):
            if isinstance(row['date'], float):
                date = datetime.fromtimestamp((row['date'] - 25569) * 86400).strftime('%d.%m.%Y')
            else:
                date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d.%m.%Y')
        else:
            date = 'NaN'

        converted_data.append({
            'id': row['id'],
            'state': row['state'],
            'date': date,
            'amount': row['amount'],
            'currency': row['currency'],
            'description': row['description'],
            'from': row['from'],
            'to': row['to']
        })

    return converted_data


def search_description_regex(data, search_string):
    """Функция для поиска строки в описании операций"""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [item for item in data if re.search(pattern, item['description'])]


def count_by_categories_collections(data, categories):
    """Функция для подсчета операций по категориям"""
    result = collections.defaultdict(int)
    for item in data:
        for category in categories:
            if category in item['description']:
                result[category] += 1
    return result
