# 1
def print_values(one: object, two: object, three: object) -> None:
    print(one, two, three)


words = "Hello", "Aloha", "Bonjour"
print_values(*words)


# 2
def count_args(*args: object) -> int:
    return len(args)


# 3
from functools import reduce
from operator import mul


def multiply(*nums: int) -> int:
    return reduce(mul, nums, 1)


# 4
from functools import reduce
from operator import add


def check_sum(*nums: int) -> None:
    if reduce(add, nums, 0) < 50:
        print("not enough")
    else:
        print("verification passed")


# 5
def is_only_one_positive(*nums: int) -> bool:
    counter = 0
    for num in nums:
        if num > 0:
            counter += 1
    return counter == 1


# 6
def print_goods(*args: object) -> None:
    for_print = list[str]()
    num = 1
    for arg in args:
        if type(arg) is str and arg:
            for_print.append(f"{num}. {arg}")
            num += 1
    if for_print:
        print(*for_print, sep="\n")
    else:
        print("Нет товаров")
