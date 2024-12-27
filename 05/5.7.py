# 1
from typing import Callable, Iterable, TypeVar

A, R = TypeVar("A"), TypeVar("R")


def apply(function: Callable[[A], R], iterable: Iterable[A]) -> list[R]:
    return [function(item) for item in iterable]


# 2
from typing import Callable, Sequence, TypeVar

V, R = TypeVar("V"), TypeVar("R")


def compute(functions: Sequence[Callable[[V], R]], *values: V) -> list[R]:
    return [function(value) for function in functions for value in values]


# 3
from functools import reduce
from typing import Any, Callable, Sequence, TypeVar

T = TypeVar("T")


def compute(functions: Sequence[Callable[[T], Any]], *values: T) -> list[Any]:
    return [
        reduce(lambda result, function: function(result), functions, value)
        for value in values
    ]


# 4
from typing import Callable, TypeVar

T = TypeVar("T")


def filter_list(func: Callable[[T], bool], lst: list[T]) -> list[T]:
    return [item for item in lst if func(item)]


# 5
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def filter_collection(
    predicate: Callable[[T], bool], items: Sequence[T]
) -> Sequence[T]:
    if type(items) is str:
        return "".join(item for item in items if predicate(item))

    return type(items)(item for item in items if predicate(item))


# 6
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def aggregation(func: Callable[[T, T], T], sequence: Sequence[T]) -> list[T]:
    if len(sequence) < 2:
        return list(sequence)

    prev = sequence[0]
    res: list[T] = []

    for index in range(1, len(sequence)):
        next = func(prev, sequence[index])
        res.append(next)
        prev = next

    return res


# 7
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def aggregation(func: Callable[[T, T], T], sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError()

    res = sequence[0]

    for index in range(1, len(sequence)):
        next = func(res, sequence[index])
        res = next

    return res


# 8
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")


def aggregation(
    func: Callable[[T, T], T], sequence: Sequence[T], initial: T | None = None
) -> T:
    if not sequence:
        raise ValueError()

    res = sequence[0] if initial is None else initial

    for index in range(1 if initial is None else 0, len(sequence)):
        next = func(res, sequence[index])
        res = next

    return res
