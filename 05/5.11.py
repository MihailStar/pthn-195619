# 1
def upper(func):
    def inner(*args, **kwargs):
        """Внутренняя функция декоратора"""
        return func(*args, **kwargs).upper()

    inner.__name__ = func.__name__
    inner.__annotations__ = func.__annotations__
    inner.__doc__ = func.__doc__

    return inner


@upper
def concatenate(*args):
    """Возвращает конкатенацию переданных строк"""
    return ", ".join(args)


print(concatenate.__name__)
print(concatenate.__doc__.strip())


# 2
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def limit_query(func: Callable[P, R]) -> Callable[P, Optional[R]]:
    limit = 3
    counter = 0

    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> Optional[R]:
        nonlocal counter
        if counter < limit:
            counter += 1
            return func(*args, **kwargs)
        print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")

    return inner


# 3
from copy import deepcopy
from functools import wraps


def no_side_effects_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        first_arg, *rest_args = args
        # @tutorial https://stepik.org/lesson/1286898/step/9?discussion=10068659&unit=1301370
        return func(deepcopy(first_arg), *rest_args, **kwargs)

    return inner


# 4
from functools import wraps


def add_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func("begin", *args, "end", **kwargs)

    return inner


# 5
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def explicit_args(func: Callable[P, R]) -> Callable[P, R | None]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R | None:
        if args:
            print(
                "Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений"
            )
            return None
        return func(*args, **kwargs)

    return inner


# 6
from functools import wraps


def reverse(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*reversed(args))

    return inner


# 7
from functools import wraps


def monkey_patching(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*("Monkey" for arg in args), **{key: "patching" for key in kwargs})

    return inner


# 8
from functools import wraps
from typing import Callable, Generic, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


class CallableWithCount(Generic[P, R]):
    def __init__(self, func: Callable[P, R]) -> None:
        self.func = func
        self.call_count = 0
        wraps(func)(self)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        self.call_count += 1
        return self.func(*args, **kwargs)


def counting_calls(func: Callable[P, R]) -> CallableWithCount[P, R]:
    return CallableWithCount(func)


# 9
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def check_count_args(func: Callable[P, R]) -> Callable[P, R | None]:
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R | None:
        if len(args) + len(kwargs) < 2:
            print("Not enough arguments")
            return
        elif len(args) + len(kwargs) > 2:
            print("Too many arguments")
            return
        else:
            return func(*args, **kwargs)

    return inner


# 10
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P, R = ParamSpec("P"), TypeVar("R")


def cache_result(func: Callable[P, R]) -> Callable[P, R]:
    cache: dict[tuple[tuple, tuple], R] = {}  # pyright: ignore

    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        cache_key = (args, tuple(kwargs.items()))

        if cache_key in cache:
            cached_result = cache[cache_key]
            print(f"[FROM CACHE] Вызов {func.__name__} = {cached_result}")
            return cached_result

        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    return inner


# 11
from functools import wraps
from typing import Callable, Generic, Literal, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


class CallableWithCount(Generic[P, R]):
    def __init__(self, func: Callable[P, R]) -> None:
        self.func = func
        self.call_count = 0
        self.calls: list[dict[Literal["args", "kwargs"], object]] = []
        wraps(func)(self)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        self.call_count += 1
        self.calls.append({"args": args, "kwargs": kwargs})
        return self.func(*args, **kwargs)


def counting_calls(func: Callable[P, R]) -> CallableWithCount[P, R]:
    return CallableWithCount(func)
