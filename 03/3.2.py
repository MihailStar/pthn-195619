# 1
def words_length(words: list[str]) -> list[int]:
    return [len(word) for word in words]


# 2
def filter_long_words(words: list[str], length: int) -> list[str]:
    return [word for word in words if len(word) > length]


# 3
from typing import TypeVar

T = TypeVar("T")


def is_member(value: T, lst: list[T]) -> bool:
    return value in lst


# 4
from typing import TypeVar

T = TypeVar("T")


def overlapping(list_a: list[T], list_b: list[T]) -> bool:
    return len(set(list_a).intersection(set(list_b))) > 0


# 5
def find_longest_word_len(words: list[str]) -> int:
    return len(max(*words, key=len))


# 6
from typing import Literal


def register_check(name_to_verdict: dict[str, Literal["no", "yes"]]) -> int:
    return sum(0 if name_to_verdict[name] == "no" else 1 for name in name_to_verdict)


# 7
from typing import TypeVar

T = TypeVar("T")


def create_tuples(list_a: list[T], list_b: list[T]) -> list[tuple[T, T]]:
    return [*zip(list_a, list_b)]


# 8
from typing import Literal


def make_header(text: str, level: Literal[1, 2, 3, 4, 5, 6]) -> str:
    return f"<h{level}>{text}</h{level}>"
