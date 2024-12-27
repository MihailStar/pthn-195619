# 1
from functools import wraps
from typing import Callable, ParamSpec

P = ParamSpec("P")


def repeater(func: Callable[P, object]) -> Callable[P, None]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> None:
        for _i in range(3):
            func(*args, **kwargs)

    return inner


# 2
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R", int, float)


def double_it(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs) * 2

    return inner


# 3
from functools import wraps
from typing import Callable, Collection, Dict, List, ParamSpec, Tuple, TypeVar, overload

P = ParamSpec("P")
K, V = TypeVar("K"), TypeVar("V")


@overload
def uppercase_elements(func: Callable[P, Dict[V, K]]) -> Callable[P, Dict[V, K]]:
    ...


@overload
def uppercase_elements(func: Callable[P, List[V]]) -> Callable[P, List[V]]:
    ...


@overload
def uppercase_elements(func: Callable[P, Tuple[V]]) -> Callable[P, Tuple[V]]:
    ...


def uppercase_elements(func: Callable[P, Collection[V]]) -> Callable[P, Collection[V]]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> Collection[V]:
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            return {
                (key.upper() if isinstance(key, str) else key): value
                for key, value in result.items()  # pyright: ignore [reportUnknownVariableType]
            }

        return type(result)(
            (item.upper() if isinstance(item, str) else item) for item in result
        )

    return inner


# 4
from functools import wraps


def first_validator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Начинаем важную проверку")
        if len(args) == 3:
            func(*args, **kwargs)
        else:
            print(f"Важная проверка не пройдена")
            return None
        print(f"Заканчиваем важную проверку")

    return inner


def second_validator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Начинаем самую важную проверку")
        if kwargs.get("name") == "Boris":
            func(*args)
        else:
            print(f"Самая важная проверка не пройдена")
            return None
        print(f"Заканчиваем самую важную проверку")

    return inner


from typing import TypeVar

V = TypeVar("V", int, float)


@second_validator
@first_validator
def sum_values(*args: V) -> None:
    print(f"Получили результат равный {sum(args)}")


sum_values(*(0, 7, 70), **{"name": "Boris"})


# 5
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def validate_all_args_str(func: Callable[P, R]) -> Callable[P, Optional[R]]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> Optional[R]:
        if any(type(arg) is not str for arg in args):
            print("Все аргументы должны быть строками")
            return None

        return func(*args, **kwargs)

    return inner


# 6
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def validate_all_args_str(func: Callable[P, R]) -> Callable[P, Optional[R]]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> Optional[R]:
        if any(type(arg) is not str for arg in args):
            print("Все аргументы должны быть строками")
            return None

        return func(*args, **kwargs)

    return inner


def validate_all_kwargs_int_pos(func: Callable[P, R]) -> Callable[P, Optional[R]]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> Optional[R]:
        if any(type(value) is not int or value < 0 for value in kwargs.values()):
            print("Все именованные аргументы должны быть положительными числами")
            return None

        return func(*args, **kwargs)

    return inner


# 7
from functools import wraps
from typing import Callable, TypeVar

R = TypeVar("R")


def filter_even(func: Callable[..., R]) -> Callable[..., R]:
    @wraps(func)
    def inner(*args, **kwargs) -> R:
        return func(
            *(
                arg
                for arg in args
                if arg is False
                or (type(arg) is int and arg % 2 == 0)
                or (hasattr(arg, "__len__") and len(arg) % 2 == 0)
            ),
            **kwargs,
        )

    return inner


def delete_short(func: Callable[..., R]) -> Callable[..., R]:
    @wraps(func)
    def inner(*args, **kwargs) -> R:
        return func(*args, **{key: kwargs[key] for key in kwargs if len(key) > 4})

    return inner
