# 1
def calculate_high_low_avg(*args: int, log_to_console: bool = False) -> float:
    low, high = min(args), max(args)
    avg = (low + high) / 2
    if log_to_console:
        print(f"{high=}, {low=}, {avg=}")
    return avg


# 2
def reserve_table(
    number: int,
    name: str,
    is_vip: bool = False,
) -> None:
    if tables[number] is None:
        tables[number] = {
            "name": name,
            "is_vip": is_vip,
            "order": {},
        }


def make_order(number: int, **kwargs: str) -> None:
    if tables[number] is None:
        return
    for category, value in kwargs.items():
        if category in ("salad", "soup", "main_dish", "drink", "desert"):
            tables[number]["order"][category] = value


# 3
def reserve_table(
    number_table: int,
    name: str,
    is_vip: bool = False,
) -> None:
    if tables[number_table] is None:
        tables[number_table] = {
            "name": name,
            "is_vip": is_vip,
            "order": {},
        }


def make_order(number_table: int, **kwargs: str) -> None:
    if tables[number_table] is None:
        return
    for category, value in kwargs.items():
        if category in ("salad", "soup", "main_dish", "drink", "desert"):
            tables[number_table]["order"][category] = value


def delete_order(
    *, number_table: int, delete_all: bool = False, **kwargs: bool
) -> None:
    if tables[number_table] is None:
        return
    if delete_all:
        tables[number_table]["order"] = {}
        return
    for category, value in kwargs.items():
        if value and category in tables[number_table]["order"]:
            del tables[number_table]["order"][category]


# 4
def reserve_table(
    number_table: int,
    name: str,
    is_vip: bool = False,
) -> None:
    if tables[number_table] is None:
        tables[number_table] = {
            "name": name,
            "is_vip": is_vip,
            "order": {},
        }


def make_order(number_table: int, **kwargs: str) -> None:
    if tables[number_table] is None:
        return
    for category, value in kwargs.items():
        if category not in ("salad", "soup", "main_dish", "drink", "desert"):
            continue
        values = value.split(",")
        tables[number_table]["order"][category] = (
            tables[number_table]["order"].get(category, []) + values
        )


def delete_order(
    *, number_table: int, delete_all: bool = False, **kwargs: bool
) -> None:
    if tables[number_table] is None:
        return
    if delete_all:
        tables[number_table]["order"] = {}
        return
    for category, value in kwargs.items():
        if value and category in tables[number_table]["order"]:
            del tables[number_table]["order"][category]
