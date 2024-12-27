# 1
english_words: tuple[str, ...] = ()
for number, english_word in enumerate(english_words, 1):
    print(f"Word № {number} = {english_word}")


# 2
from typing import Iterable


def even_items(items: Iterable[int]) -> list[int]:
    return [item for index, item in enumerate(items) if index % 2 == 1]


# 3
def get_words_with_position(words: str) -> list[tuple[str, int]]:
    return [(word, number) for number, word in enumerate(words.split(), 1)]


# 4
def find_different_indexes(string_a: str, string_b: str) -> list[int]:
    return [
        index
        for index, chars in enumerate(zip(string_a, string_b))
        if chars[0] != chars[1]
    ]


# 5
# Алгоритм Луна (Luhn algorithm)
def luhn_algorithm(card_number: int) -> bool:
    temp = [int(digit) for digit in str(card_number)]
    for index in range(0, len(temp), 2):
        temp[index] *= 2
        if temp[index] > 9:
            temp[index] -= 9
    return sum(temp) % 10 == 0
