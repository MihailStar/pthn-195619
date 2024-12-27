# 1
from typing import Generator


def gen_odd(n: int) -> Generator[int, None, None]:
    for odd in range(1, n + 1, 2):
        yield odd


# 2
from typing import Generator


def alphabet() -> Generator[tuple[str, str], None, None]:
    for letter, word in DICTIONARY.items():
        yield (letter, word)


# 3
from typing import Generator


def my_range_gen(n: int) -> Generator[int, None, None]:
    for num in range(n):
        yield num


# 4
from typing import Generator


def gen_squares(n: int) -> Generator[int, None, None]:
    for num in range(1, n + 1):
        yield num**2


# 5
from typing import Generator, NoReturn


def gen_arithmetic_progression(
    first: int, difference: int
) -> Generator[int, None, NoReturn]:
    n = first
    while True:
        yield n
        n += difference


# 6
# Последовательность Фибоначчи (Fibonacci sequence)
from typing import Generator


def gen_fibonacci_numbers(n: int) -> Generator[int, None, None]:
    """
    @tutorial https://github.com/MihailStar/pthn-244/blob/53e66ac5e3f892f3515a557c61661af93cec8ca5/src/15.py#L4
    @tutorial https://github.com/MihailStar/pthn-58852/blob/4c3ce9e31780f7f7ca891ee2f6ed16c20d54cccc/07/7.3.py#L109
    """
    f0, f1 = 0, 1
    for _i in range(n):
        f0, f1 = f1, f0 + f1
        yield f0


# 7
from functools import cache
from math import factorial
from typing import Generator

# @tutorial https://github.com/MihailStar/pthn-133387/blob/4401f1b8ad5fb0213707af427a3bd7a4a345d21b/05/5.2.py#L31
fuctorial = cache(factorial)


def gen_factorial(n: int) -> Generator[int, None, None]:
    for num in range(1, n + 1):
        yield fuctorial(num)


# 8
from functools import cache
from math import factorial
from typing import Generator

# @tutorial https://github.com/MihailStar/pthn-133387/blob/4401f1b8ad5fb0213707af427a3bd7a4a345d21b/05/5.2.py#L31
fucktorial = cache(factorial)


def gen_factorial() -> Generator[int, None, None]:
    n = 1
    while True:
        yield fucktorial(n)
        n += 1


# 9
from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def my_enumerate(
    items: Iterable[T], start: int = 0
) -> Generator[tuple[int, T], None, None]:
    index = start
    for item in items:
        yield (index, item)
        index += 1


# 10
from typing import Generator, Sequence, TypeVar

T = TypeVar("T")


def chunker(sequence: Sequence[T], size: int) -> Generator[Sequence[T], None, None]:
    starting_index = 0
    while True:
        chunk = sequence[starting_index : starting_index + size]
        if not chunk:
            break
        yield chunk
        starting_index += size


# 11
from typing import Generator, overload


@overload
def my_range_gen(stop: int, /) -> Generator[int, None, None]:
    ...


@overload
def my_range_gen(start: int, stop: int, /) -> Generator[int, None, None]:
    ...


def my_range_gen(start: int, stop: int | None = None) -> Generator[int, None, None]:
    if stop is None:
        stop, start = start, 0
    for num in range(start, stop):
        yield num


# 12
from typing import Generator, overload


@overload
def my_range_gen(stop: int, /) -> Generator[int, None, None]:
    ...


@overload
def my_range_gen(start: int, stop: int, /) -> Generator[int, None, None]:
    ...


@overload
def my_range_gen(start: int, stop: int, step: int, /) -> Generator[int, None, None]:
    ...


def my_range_gen(
    start: int, stop: int | None = None, step: int = 1
) -> Generator[int, None, None]:
    if stop is None:
        start, stop = 0, start
    current = start
    while (step < 0 and current > stop) or (step > 0 and current < stop):
        yield current
        current += step
