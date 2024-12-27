# 1
from inspect import getgeneratorstate
from typing import Generator


def my_coro(a: int) -> Generator[int, int, None]:
    print(f"Запускаем корутину со значением a={a}")
    b = yield a
    print(f"Получено значение b={b}")
    c = yield a + b
    print(f"Получено значение c={c}")


coro = my_coro(7)
print(getgeneratorstate(coro))
next(coro)
print(getgeneratorstate(coro))
print(coro.send(23))
print(getgeneratorstate(coro))
try:
    print(coro.send(100))
except StopIteration:
    pass
print(getgeneratorstate(coro))


# 2
from typing import Generator, NoReturn


def alphabet() -> Generator[str, str, NoReturn]:
    sended_key = yield ""
    while True:
        try:
            sended_key = yield DICTIONARY.get(sended_key, "default")
        except KeyError:
            sended_key = yield "default"
