# 1
from typing import Callable


def multiply(a: float) -> Callable[[float], float]:
    def inner(b: float) -> float:
        return a * b

    return inner


# 2
from typing import Callable


def make_repeater(n: int) -> Callable[[str], str]:
    def inner(s: str) -> str:
        return n * s

    return inner


# 3, 4
from typing import Callable


def create_accumulator(initial: float = 0) -> Callable[[float], float]:
    accumulator = initial

    def inner(n: float) -> float:
        nonlocal accumulator
        accumulator += n
        return accumulator

    return inner


# 5
from typing import Callable


def countdown(limit: int = 0) -> Callable[[], None]:
    counter = limit

    def inner() -> None:
        nonlocal counter
        print(
            counter if counter > 0 else f"Превышен лимит, вы вызвали более {limit} раз"
        )
        counter -= 1

    return inner


# 6
from typing import Callable


def count_calls() -> Callable[[], None]:
    def inner() -> None:
        setattr(inner, "total_calls", getattr(inner, "total_calls") + 1)

    setattr(inner, "total_calls", 0)

    return inner

# 6
class CallableWithTotalCalls:
    total_calls = 0

    def __call__(self) -> None:
        self.total_calls += 1


def count_calls() -> CallableWithTotalCalls:
    return CallableWithTotalCalls()


# 7
from typing import Callable


def create_dict() -> Callable[[object], dict[int, object]]:
    d: dict[int, object] = {}
    key = 0

    def inner(o: object) -> dict[int, object]:
        nonlocal key
        key += 1
        d[key] = o
        return d

    return inner
