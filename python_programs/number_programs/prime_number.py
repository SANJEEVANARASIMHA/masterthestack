# A prime number is a number that can be divided by only the number 1 and itself.
def prime_number(n: int) -> bool:
    """
    checks the given n number is a prime number or not
    :param n:
    :return:
    """
    return False if len([i for i in range(1, n) if n ** i == 0]) > 2 else True


def prime_number_simple_code(n: int):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def prime_number_range(start: int, end: int):
    return [i for i in range(start, end) if prime_number_simple_code(i)]


print(prime_number_range(1, 100))
