# 1
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R", int, float)


def multiply_result_by(n: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs) * n

        return inner

    return decorator


# 2
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def limit_query(limit: int) -> Callable[[Callable[P, R]], Callable[P, R | None]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R | None]:
        counter = 0

        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R | None:
            nonlocal counter
            if counter < limit:
                counter += 1
                return func(*args, **kwargs)
            print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")

        return inner

    return decorator


# 3
from functools import wraps


def monkey_patching(arg: str = "Monkey", kwarg: str = "patching"):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*(arg for value in args), **{key: kwarg for key in kwargs})

        return inner

    return decorator


# 4
from functools import wraps


def pass_arguments(*passed_args, **passed_kwargs):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, *passed_args, **kwargs, **passed_kwargs)

        return inner

    return decorator


# 5
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def convert_to(
    type_: Callable[..., R]
) -> Callable[[Callable[P, object]], Callable[P, R]]:
    def decorator(func: Callable[P, object]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            return type_(func(*args, **kwargs))

        return inner

    return decorator


# 6
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def validate_all_args(
    type_: object,
) -> Callable[[Callable[P, R]], Callable[P, R | None]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R | None]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R | None:
            if any(type(arg) is not type_ for arg in args):
                print(f"Все аргументы должны принадлежать типу {type_}")
                return None
            return func(*args, **kwargs)

        return inner

    return decorator


# 7
from functools import reduce, wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def compose(*callables: Callable[[R], R]) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            return reduce(
                lambda res, callable: callable(res), callables, func(*args, **kwargs)
            )

        return inner

    return decorator


# 8
from functools import wraps


def add_attrs(**attributes: object):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        for key, value in attributes.items():
            setattr(inner, key, value)

        return inner

    return decorator
