# 1
from typing import Generator, NoReturn


def grep(pattern: str) -> Generator[None, str, NoReturn]:
    while True:
        sended_text = yield None
        if pattern in sended_text.lower():
            print(sended_text)


# 2
from typing import Generator, NoReturn


def alphabet() -> Generator[str, str, NoReturn]:
    sended_key = ""
    while True:
        sended_key = yield DICTIONARY.get(sended_key, "")


# 3
from typing import Generator, NoReturn


def is_palindrome() -> Generator[bool, int, NoReturn]:
    sended_number = yield False
    while True:
        sended_number = yield str(sended_number) == "".join(
            reversed(str(sended_number))
        )


# 4
from typing import Generator, NoReturn


def get_average() -> Generator[float, float, NoReturn]:
    sended_number = yield 0.0
    total = 0.0
    number_of = 0
    while True:
        total += sended_number
        number_of += 1
        sended_number = yield total / number_of


# 5
from typing import Generator, NoReturn


def check_password() -> Generator[bool, str, NoReturn]:
    sended_password = yield False
    while True:
        is_secure = (
            len(sended_password) > 9
            and any(char.isupper() for char in sended_password)
            and any(char.isdigit() for char in sended_password)
            and any(char in ("!", "@", "#", "$", "%") for char in sended_password)
        )
        sended_password = yield is_secure
