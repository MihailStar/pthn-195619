# 1
def print_histogram(columns: list[int]) -> None:
    for column in columns:
        print("*" * column)


# 2
def count_words(string: str) -> int:
    return len(string.split())
