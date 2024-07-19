import logging

log_file_path = 'C:/Users/Александр Побережный/Desktop/питон/course_2/logs/app.log'

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
"""Настройка логгера"""

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
"""Создание обработчика для записи логов в файл"""

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
"""Создание форматтера для логов"""

logger.addHandler(file_handler)
"""Добавление обработчика к логгеру"""


def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера карты"""
    return number[:4] + " " + number[4:6] + '** **** ' + number[-4:]


def get_mask_account(number: str) -> str:
    """Функция маскировки номера счета"""
    return '*' * (len(number) - 18) + number[-4:]


masked_card = get_mask_card_number('1234567890123456')
masked_account = get_mask_account('73654108430135874305')


logger.info('Маскированный номер карты: %s', masked_card)
logger.info('Маскированный номер счета: %s', masked_account)
