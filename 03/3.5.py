# 1
def words_length(words: list[str]) -> None:
    for index in range(len(words)):
        words[index] = len(words[index])


# 2
def my_func(collection: list[int], n: int) -> list[int]:
    result = collection[::]
    for i in range(1, n + 1):
        result.append(i)
    return result


# 3
from typing import TypeVar

T = TypeVar("T")


def lstrip(lst: list[T], value: T) -> None:
    while lst and lst[0] == value:
        lst.pop(0)


# 4
from typing import TypeVar

T = TypeVar("T")


def lstrip(lst: list[T], value: T) -> list[T]:
    result = lst.copy()
    while result and result[0] == value:
        result.pop(0)
    return result
