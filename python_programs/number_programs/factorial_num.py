def factorial_num(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def factorial_recursive(n: int) -> int:
    n = [1 if n == 0 or n == 1 else n * factorial_recursive(n - 1)]
    return n[0]


print(factorial_recursive(5))
