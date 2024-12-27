# 1
def print_scores(name: str, *scores: int) -> None:
    print(f"Student name: {name}")
    print(*sorted(scores), sep="\n")


# 2
def truncate_sentences(n: int, *strings: str) -> None:
    for string in strings:
        print(string[:n])


# 3
def make_strings_big(*strings: str, reverse: bool = False) -> None:
    for string in strings:
        if reverse:
            print(string.lower())
        else:
            print(string.upper())
