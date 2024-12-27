# 1
from typing import TypeAlias

NestedList: TypeAlias = list["int | NestedList"]


def sum_recursive(nested: NestedList) -> int:
    return sum(
        sum_recursive(item) if isinstance(item, list) else item for item in nested
    )


# 2
from typing import TypeAlias

NestedList: TypeAlias = list["int | str | NestedList"]


def multu_recursive(nested: NestedList) -> int:
    result = 1

    for item in nested:
        if isinstance(item, list):
            result *= multu_recursive(item)
        elif isinstance(item, int):
            result *= item

    return result


# 3
from math import inf
from typing import TypeAlias

NestedList: TypeAlias = list["int | NestedList"]


def get_max_recursive(nested: NestedList) -> int:
    ma = -inf

    for item in nested:
        if isinstance(item, list):
            item = get_max_recursive(item)
        if item > ma:
            ma = item

    return int(ma)


# 4
from typing import TypeAlias

NestedList: TypeAlias = list["int | NestedList"]


def flatten(nested: NestedList) -> list[int]:
    result: list[int] = []

    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
            continue
        result.append(item)

    return result


# 5
from typing import TypeAlias

NestedList: TypeAlias = list["object | NestedList"]


def is_member(value: object, nested: NestedList) -> bool:
    for item in nested:
        if isinstance(item, list) and is_member(value, item):
            return True
        if value == item:
            return True

    return False


# 6
from typing import TypeAlias

NestedList: TypeAlias = list["object | NestedList"]


def find_level_element(value: object, nested: NestedList) -> int:
    def _find_level_element(value: object, nested: NestedList, level: int = 1) -> int:
        """
        @tutorial AI
        """
        for item in nested:
            if isinstance(item, list):
                if (result := _find_level_element(value, item, level + 1)) != -1:
                    return result
            elif value == item:
                return level

        return -1

    return _find_level_element(value, nested)


# 7
from typing import TypeAlias

NestedList: TypeAlias = list["int | NestedList"]


def reversed_recursive(nested: NestedList) -> NestedList:
    result: NestedList = []

    for item in nested:
        result.insert(0, reversed_recursive(item) if isinstance(item, list) else item)

    return result


# 8
from typing import TypeAlias

NestedDict: TypeAlias = dict[str, "int | NestedDict"]


def flatten_dict(nested: NestedDict) -> dict[str, int]:
    result: dict[str, int] = {}
    key_separator = "_"

    def _flatten_dict(nested: NestedDict, key_prefix: str = "") -> None:
        """
        @tutorial AI
        """
        for key, value in nested.items():
            if isinstance(value, dict):
                _flatten_dict(value, key_prefix + key + key_separator)
            else:
                result[key_prefix + key] = value

    _flatten_dict(nested)

    return result
