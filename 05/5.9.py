# 1
from functools import wraps
from typing import Callable, ParamSpec

P = ParamSpec("P")


def uppercase(func: Callable[P, str]) -> Callable[P, str]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> str:
        return func(*args, **kwargs).upper()

    return inner


@uppercase
def calculate_tax(name: str, income: float, tax_rate: float) -> str:
    tax = income - income * (1 - tax_rate / 100)
    return f"{name} должен заплатить налог {tax}$"


print(calculate_tax("Ivan", 5000, 25))
print(calculate_tax("vaSilIy", 15000, 30))
print(calculate_tax("depardieu", 215000, 40))


# 2
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def decorator(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print("---Start calculation---")
        result = func(*args, **kwargs)
        print(f"---Finish calculation. Result is {result}---")
        return result

    return inner


@decorator
def add(a: int, b: int) -> int:
    return a + b


# 3
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def decorator(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print("---Start calculation---")
        result = func(*args, **kwargs)
        print(f"---Finish calculation. Result is {result}---")
        return result

    return inner
