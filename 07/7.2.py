# 1
def summa(n: int) -> int:
    if n > 1:
        return n + summa(n - 1)
    return 1


# 2
def find_min(ns: list[int]) -> int:
    if len(ns) == 1:
        return ns[0]
    mi = find_min(ns[1:])
    return ns[0] if ns[0] < mi else mi


# 3
def sum_recursive(ns: list[int]) -> int:
    if len(ns) == 1:
        return ns[0]
    return ns[0] + sum_recursive(ns[1:])


# 4
def sum_digits(n: int) -> int:
    if n % 10 == n:
        return n
    return n % 10 + sum_digits(n // 10)


# 5
def double_fact(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * double_fact(n - 2)


# 6
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 7
def tribonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# 8
def get_combin(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


# 9
def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))
