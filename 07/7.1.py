# 1
def speller(word: str) -> None:
    if len(word) > 0:
        speller(word[1:])
        print(word[0])


# 2
def print_from(n: int) -> None:
    if n < 1:
        return
    print(n)
    print_from(n - 1)


# 3
def print_to(n: int) -> None:
    if n < 1:
        return
    print_to(n - 1)
    print(n)
