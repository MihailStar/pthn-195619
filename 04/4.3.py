# 1
from collections import defaultdict
from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    """Находит первый дубль в списке"""
    counter = defaultdict[str, int](int)
    for word in words:
        if counter[word] == 1:
            return word
        counter[word] = 1


# 2
def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    """Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"""
    if not lst:
        return lst
    normalized_shift = shift % len(lst)
    return lst[-normalized_shift:] + lst[:-normalized_shift]


# 3
def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    """Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)"""
    if not tpl:
        return tpl
    normalized_shift = shift % len(tpl)
    return tpl[-normalized_shift:] + tpl[:-normalized_shift]


# 4
def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    alphabet_size = 26
    return chr((ord(letter) - ord("a") + shift) % alphabet_size + ord("a"))


# 5
def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    alphabet_size = 26
    return chr((ord(letter) - ord("a") + shift) % alphabet_size + ord("a"))


def caesar_cipher(phrase: str, key: int) -> str:
    """Шифр Цезаря"""
    result = ""
    for char in phrase:
        result += rotate_letter(char, key) if char.isalpha() else char
    return result
