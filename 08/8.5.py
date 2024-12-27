# 1
from typing import Generator, TypeVar

T = TypeVar("T")


def flatten_matrix(nested_list: list[list[T]]) -> Generator[T, None, None]:
    for row in nested_list:
        yield from row


# 2
from typing import Generator, TypeAlias

NestedList: TypeAlias = int | list["NestedList"]


def flatten(nested: NestedList) -> Generator[int, None, None]:
    if isinstance(nested, list):
        for item in nested:
            yield from flatten(item)
    else:
        yield nested

# 2
from typing import Generator, TypeAlias

NestedList: TypeAlias = list["int | NestedList"]


def flatten(nested: NestedList) -> Generator[int, None, None]:
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
