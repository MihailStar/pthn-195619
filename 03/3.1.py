# 1
def powers(num: int) -> list[int]:
    square = num**2
    cube = num**3
    return [num, square, cube]


# 2
def is_adult(age: int) -> bool:
    return age > 17


if is_adult(int(input())):
    print("Ух какой большой")
else:
    print("Подрасти еще, сынок")


# 3
from calendar import isleap

is_leap = isleap


# 4
def is_palindrome(s: str) -> bool:
    lowered_chars = [char.lower() for char in s if char.isalpha()]
    return lowered_chars == lowered_chars[::-1]


# 5
from calendar import isleap


def count_leap_years(year_a: int, year_b: int) -> int:
    counter = 0
    for year in range(year_a, year_b):
        if isleap(year):
            counter += 1
    return counter


# 6
from calendar import isleap


def get_leap_years(year_a: int, year_b: int) -> list[int]:
    result: list[int] = []
    for year in range(year_a, year_b):
        if isleap(year):
            result.append(year)
    return result


# 7
def create_palindrome(s: str) -> str:
    chars = s.lower()
    reversed_chars = chars[::-1]
    if chars == reversed_chars:
        return chars
    return f"{chars}_i_{reversed_chars}"


# 8
def is_strings_equal(string_a: str, string_b: str) -> bool:
    if len(string_a) != len(string_b):
        return False
    return sorted(string_a) == sorted(string_b)


# 9
from re import fullmatch


def is_dunder(maybe_dunder: str) -> bool:
    return fullmatch(r"__[A-Za-z]{2}[A-Za-z]*__", maybe_dunder) is not None
