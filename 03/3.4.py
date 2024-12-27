# 1
def replace(text: str, old: str, new: str = "") -> str:
    return text.replace(old, new)


# 2
from functools import reduce
from operator import mul


def product(nums: list[int], start: int = 1) -> int:
    return reduce(mul, nums, start)


# 3
shopping_list: dict[str, int] = {}


def add_item(name: str, number_of: int = 1) -> None:
    shopping_list[name] = shopping_list.get(name, 0) + number_of


# 4
shopping_list: dict[str, int] = {}


def show_list(include_quantities: bool = True) -> None:
    if include_quantities:
        for name, number_of in shopping_list.items():
            print(f"{number_of}x{name}")
    else:
        for name in shopping_list:
            print(name)


# 5
from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    marks: list[int]


def create_student(name: str, age: int, marks: list[int] | None = None) -> Student:
    marks = marks if marks else []
    return {"name": name, "age": age, "marks": marks}


def add_mark(student: Student, mark: int) -> None:
    student["marks"].append(mark)


# 6
def calculate_per_person(bill_sum: float, number_of_person: int, ch: int = 10) -> float:
    return round((bill_sum + (bill_sum / 100 * ch)) / number_of_person, 2)


# 7
def reserve_table(number: int, name: str, is_vip: bool = False) -> None:
    if tables[number] is None:
        tables[number] = {"name": name, "is_vip": is_vip}


# 8
def create_matrix(
    size: int = 3, up_fill: int = 0, down_fill: int = 0
) -> list[list[int]]:
    matrix: list[list[int]] = []
    for y in range(size):
        row: list[int] = []
        for x in range(size):
            if y > x:
                row.append(down_fill)
            elif y < x:
                row.append(up_fill)
            else:
                row.append(y + 1)
        matrix.append(row)
    return matrix
