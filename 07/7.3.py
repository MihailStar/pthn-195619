# 1
from typing import TypeVar

T = TypeVar("T")


def is_member(value: T, lst: list[T]) -> bool:
    if not lst:
        return False
    return value == lst[0] or is_member(value, lst[1:])


# 2
def power(a: int, n: int) -> int:
    if n == 1:
        return a
    return a * power(a, n - 1)


# 3
from math import gcd


# 4
def is_palindrome(symbols: str) -> bool:
    if not symbols:
        return True
    return symbols[0].lower() == symbols[-1].lower() and is_palindrome(symbols[1:-1])


# 5
def get_arith_progression(n: int) -> int:
    if n == 1:
        return 1
    return 7 + get_arith_progression(n - 1)


# 6
def get_arith_progression(a1: int, d: int, n: int) -> int:
    if n == 1:
        return a1
    return get_arith_progression(a1 + d, d, n - 1)


# 7
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def state_printer(func: Callable[[int, int], T]) -> Callable[[int, int], T]:
    @wraps(func)
    def wrapper(a: int, n: int) -> T:
        print(f"State: {a=}, {n=}")
        return func(a, n)

    return wrapper


@state_printer
def quick_power(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        sqrt = quick_power(a, n // 2)
        return sqrt * sqrt
    return a * quick_power(a, n - 1)

# 7
from functools import wraps
from itertools import chain
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def state_printer(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(
            # @tutorial https://stepik.org/lesson/1252721/step/9?discussion=10171013&thread=solutions&unit=1266620
            f"State: {', '.join(f'{name}={value}' for name, value in chain(zip(func.__code__.co_varnames, args), kwargs.items()))}"
        )

        return func(*args, **kwargs)

    return wrapper


@state_printer
def quick_power(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        sqrt = quick_power(a, n // 2)
        return sqrt * sqrt
    return a * quick_power(a, n - 1)
