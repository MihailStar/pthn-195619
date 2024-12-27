# 1
from typing import Callable


def outer() -> tuple[Callable[[], None], Callable[[], None]]:
    def say_hello() -> None:
        print("hello")

    def say_bye() -> None:
        print("bye")

    return (say_hello, say_bye)


say_hello, say_bye = outer()

say_hello()
say_bye()


# 2
from typing import Callable


def wrap_increment(value: int) -> int:
    _inc: Callable[[int], int] = lambda value: value + 1

    return _inc(value)


# 3
def get_extensions(file_names: list[str]) -> list[str]:
    def _get_extension(file_name: str) -> str:
        if "." in file_name:
            return file_name.split(".")[-1]
        return ""

    return [_get_extension(file_name) for file_name in file_names]


# 4
def double_odd_numbers(numbers: list[int]) -> list[int]:
    def is_odd(number: int) -> bool:
        return number % 2 == 0

    def double(number: int) -> int:
        return number * 2

    return [double(number) for number in numbers if not is_odd(number)]


# 5
from operator import add, mul, sub, truediv
from typing import Literal


def calculate(x: float, y: float, operation: Literal["a", "s", "d", "m"] = "a") -> None:
    addition, subtraction, division, multiplication = add, sub, truediv, mul

    match operation:
        case "a":
            print(addition(x, y))
        case "s":
            print(subtraction(x, y))
        case "d":
            if y == 0:
                print("На ноль делить нельзя!")
            else:
                print(division(x, y))
        case "m":
            print(multiplication(x, y))
        case _:
            print("Ошибка. Данной операции не существует")
