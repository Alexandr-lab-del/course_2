from src.decorators import log
from typing import Union


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x / y


my_function(1, 0)
