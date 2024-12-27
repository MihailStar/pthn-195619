# 1
def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# 2
def repeat_phrase_n_times(phrase: str, n: int) -> None:
    for _ in range(n):
        print(phrase)
