import logging
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable:
    """Внешняя функция, которая принимает аргумент для указания имени файла, в который будет записываться информация"""
    def decorator_log(func: Callable) -> Callable:
        """Декоратор, который приниает функцию в качестве аргумента и определяет функцию обертку"""
        @wraps(func)
        def wrapper_log(*args: Any, **kwargs: Any) -> Any:
            """Функция обертка, которая формирует строку с именем функции, записывает результат выполнения функции
             и выводит ответ в зависимости от параметра filename"""
            log_message = f"{func.__name__} "
            try:
                result = func(*args, **kwargs)
                log_message += "ok"
            except Exception as e:
                log_message += f"error: {str(e)}. Inputs: {args}, {kwargs}"
                result = None

            if filename:
                logging.basicConfig(filename=filename, level=logging.INFO)
                logging.info(log_message)
            else:
                print(log_message)

            return result

        return wrapper_log

    return decorator_log
