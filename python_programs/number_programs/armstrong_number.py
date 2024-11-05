# An Armstrong number is a special kind of number in math.
# It's a number that equals the sum of its digits, each raised to a power.
# For example, if you have a number like 153, it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.

def armstrong_number(n: int) -> bool:
    """
    checks the given number is an arm strong number or not
    :param n:
    :return bool: True or False
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    result = 0
    input_n = n
    n_length = len(str(n))
    while n:
        result = result + (n % 10) ** n_length
        n = n // 10
    return True if input_n == result else False


def armstrong_number_with_simple_code(n: int)-> bool:
    """Check if the given number is an Armstrong number. by using the list comprension we can make it as simple"""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    input_n, n_length = n, len(str(n))
    result = sum((int(digit) ** n_length for digit in str(n)))
    return input_n == result


def find_armstrong_number_from_range(start: int, end: int) -> list:
    """
    returns arm strong number if it is present in between the range of start and end
    :param start: start of range
    :param end: end of range
    :return: list
    """
    if not isinstance(start, int):
        raise TypeError("start must be an integer")
    if not isinstance(end, int):
        raise TypeError("end must be an integer")
    arm_numbers = [i for i in range(start, end) if armstrong_number(i)]
    return arm_numbers

print(find_armstrong_number_from_range(100, 1000))
