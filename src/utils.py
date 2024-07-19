import os
import json
import logging
from logging.handlers import RotatingFileHandler

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
    """ Читает данные о транзакциях из JSON файла по указанному пути и возвращает список транзакций."""
    transactions = []
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден")
        return transactions

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                transactions = data
        except json.JSONDecodeError:
            logger.error("Ошибка чтения JSON файла")
    logger.info(f"Прочитано {len(transactions)} транзакций из файла {file_path}")
    return transactions


transactions = read_transactions("transactions.json")
