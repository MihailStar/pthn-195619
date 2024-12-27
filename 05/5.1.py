# 1
from typing import Callable, Literal


def red() -> Literal["Color is red"]:
    return "Color is red"


def green() -> Literal["Color is green"]:
    return "Color is green"


def blue() -> Literal["Color is blue"]:
    return "Color is blue"


colors: dict[Callable[[], str], str] = {}
colors[green] = "00FF00"
colors[blue] = "0000FF"
colors[red] = "FF0000"

for key_func in colors:
    print(f"{key_func()} - {colors[key_func]}")


# 2
import math
from functools import wraps
from typing import Callable, TypeVar

A, R = TypeVar("A"), TypeVar("R")


def caching_decorator(func: Callable[[A], R]) -> Callable[[A], R]:
    cache: dict[A, R] = {}

    @wraps(func)
    def inner(arg: A) -> R:
        if arg in cache:
            print(f"Get from cache value {func.__name__}({arg})")
            return cache[arg]

        result = func(arg)
        cache[arg] = result

        return result

    return inner


factorial = caching_decorator(math.factorial)
