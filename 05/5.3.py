# 1
from typing import Callable

square: Callable[[int, int], int] = lambda x, y: x**2 + y**2


# 2
from typing import Callable

adding_10: Callable[[int], int] = lambda n: n + 10


# 3
from typing import Callable

starts_with: Callable[[str], bool] = lambda s: s[0] == "W"


# 4
from typing import Callable

check_word: Callable[[str], bool] = (
    lambda s: s.upper().startswith(("Q", "R"))
    and s.upper().endswith(("A", "E", "I", "U", "O"))
)


# 5
from calendar import isleap
from typing import Callable

is_leap: Callable[[int], bool] = lambda y: isleap(y)


# 6
from typing import Callable

sale_lambda: Callable[[float], float] = lambda x: x * 0.9


# 7
from typing import Callable

sale_lambda: Callable[[float], float] = lambda x: x * 0.9 if x > 50 else x


# 8
from statistics import mean
from sys import version_info
from typing import Callable

if version_info < (3, 11):
    average: Callable[..., float]
else:
    from typing import Unpack

    average: Callable[[Unpack[tuple[int, ...]]], float]

average = lambda *args: float(mean(args))
