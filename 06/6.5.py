# 1
keys = [
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
    "One hundred",
]
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print({k: v for k, v in zip(keys, values)})


# 2
def create_info(employees: list[str], identifiers: list[str]) -> dict[str, str]:
    return {k: v for k, v in zip(sorted(identifiers), sorted(employees))}


# 3
from typing import Callable, TypeVar

T = TypeVar("T")


def zip_with_function(for_zip: list[list[int]], function: Callable[..., T]) -> list[T]:
    return [function(*arguments) for arguments in zip(*for_zip)]


# 4
def get_info_marks(students: list[str], *marks: list[int]) -> dict[str, int]:
    return {student: max(mark) for student, *mark in zip(students, *marks)}


# 5
from typing import Literal


def get_info_marks(
    students: list[str], *marks: list[int]
) -> dict[str, dict[Literal["best", "worst"], int]]:
    return {
        student: {"best": max(student_marks), "worst": min(student_marks)}
        for student, *student_marks in zip(students, *marks)
    }
