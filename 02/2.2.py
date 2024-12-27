# 1
def get_max(a: int, b: int) -> int:
    return max(a, b)


# 2
from functools import reduce
from operator import mul


def multiply(nums: list[int]) -> int:
    return reduce(mul, nums, 1)


# 3
def get_reverse(string: str) -> str:
    return "".join(reversed(list(string)))


# 4
def generate_n_chars(n: int, s: str) -> str:
    return n * s
