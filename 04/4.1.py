# 1
def add_binary(a: int, b: int) -> str:
    """Возвращает сумму чисел a и b в двоичном виде"""
    binary_sum = bin(a + b)[2:]
    return binary_sum
