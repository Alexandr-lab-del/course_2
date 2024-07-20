import json
import logging
from logging.handlers import RotatingFileHandler
from openpyxl import load_workbook
import pandas as pd


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
"""Настройка логгера"""

formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
"""Создание форматтера для логов"""

log_file_path = 'logs/app.log'
file_handler = RotatingFileHandler(log_file_path, mode='w', maxBytes=1e6, backupCount=1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
"""Создание обработчика для записи логов в файл"""

logger.addHandler(file_handler)
"""Добавление обработчика к логгеру"""


def read_transactions(file_path):
    """Чтение транзакций из файлов"""
    transactions = []
    if file_path.endswith('.json'):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    transactions = data
            except json.JSONDecodeError:
                logger.error("Ошибка чтения JSON файла")

    elif file_path.endswith('.csv'):
        transactions = pd.read_csv(file_path, delimiter=';').to_dict(orient='records')

    elif file_path.endswith('.xlsx'):
        wb = load_workbook(file_path)
        sheet = wb.active
        data = sheet.values
        columns = next(data)[0:]
        transactions = [dict(zip(columns, row)) for row in data]

    else:
        logger.error("Неподдерживаемый формат файла")

    logger.info(f"Прочитано {len(transactions)} транзакций из файла {file_path}")
    return transactions
