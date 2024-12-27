# 1
def print_args(a: object, b: object, c: object, d: object) -> None:
    print(a, b, c, d)


dct = {"a": 100, "b": 200, "c": 300, "d": 400}
print_args(**dct)


# 2
def concatenate(**kwargs: str) -> str:
    return "".join(map(str, kwargs.values()))


# 3
def create_actor(**kwargs: object) -> dict[str, object]:
    return {
        **{"name": "Райан", "surname": "Рейнольдс", "age": 47},
        **kwargs,
    }


# 4
def info_kwargs(**kwargs: object) -> None:
    for key in sorted(kwargs):
        print(f"{key} = {kwargs[key]}")
