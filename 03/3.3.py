# 1
alpha = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(s: str) -> bool:
    d: dict[str, str] = {c: c for c in s.lower() if c in alpha}
    return len(d) == 26


# 2
from string import ascii_lowercase

vowels = "aeiou"
not_vowels = set(ascii_lowercase).difference(set(vowels))


def translate_to_robber_lang(s: str) -> str:
    return "".join(
        f"{char}o{char}" if char.lower() in not_vowels else char for char in s
    )


# 3
def is_table_free(n: int) -> bool:
    return tables[n] is None


def get_free_tables() -> list[int]:
    return [n for n in tables if tables[n] is None]


# 4
def reserve_table(n: int, name: str) -> None:
    if tables[n] is None:
        tables[n] = name


def delete_reservation(n: int) -> None:
    tables[n] = None


# 5
def reserve_table(n: int, name: str, is_vip: bool) -> None:
    if tables[n] is None:
        tables[n] = {"name": name, "is_vip": is_vip}


def delete_reservation(n: int) -> None:
    tables[n] = None
