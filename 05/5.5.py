# 1
def get_info_about_object(o: object) -> None:
    print(dir(o))
    print(f"Всего у объекта {len(dir(o))} атрибутов и методов")


# 2
def check_exist_attrs(o: object, attributes: list[str]) -> dict[str, bool]:
    true_attributes = dir(o)
    return {attribute: attribute in true_attributes for attribute in attributes}


# 3
def create_attrs(o: object, attributes: list[tuple[str, object]]) -> None:
    for attribute, value in attributes:
        o.__setattr__(attribute, value)


def check_exist_attrs(o: object, attributes: list[str]) -> dict[str, bool]:
    true_attributes = o.__dir__()
    return {attribute: attribute in true_attributes for attribute in attributes}


# 4
def count_strings(*args: object) -> int:
    count = 0
    for arg in args:
        if type(arg) is str:
            count += 1
    return count


# 5
def find_keys(**kwargs: object) -> list[str]:
    return sorted(
        (arg for arg, value in kwargs.items() if isinstance(value, (list, tuple))),
        key=str.lower,
    )
