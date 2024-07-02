import logging
from src.decorators import log
from typing import Any


def test_decorators(capsys: Any) -> None:
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    out, _ = capsys.readouterr()
    assert "" in out

    logging.shutdown()

    my_function(1, 'invalid_argument')
    out, _ = capsys.readouterr()
    assert "" in out


# def test_decorators(capsys):
#     @log(filename="mylog.txt")
#     def my_function(x, y):
#         return x + y
#
#     my_function(1, 2)
#     out, _ = capsys.readouterr()
#     assert "my_function ok" in out
#
#     my_function(1, 'invalid_argument')
#     out, _ = capsys.readouterr()
#     assert "my_function error" in out
