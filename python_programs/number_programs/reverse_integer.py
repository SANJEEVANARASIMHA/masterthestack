def reverse_integer_with_trailing_zeros(n: int) -> str:
    """
    :param n: integer value
    :return: string
    """
    if not isinstance(n, int):
        raise TypeError("The parameter must be an integer.")
    # if n is an - intger then this will help to return negative reversed number
    sign = '-' if n < 0 else ''
    n = abs(n)
    reversed_str = ''
    while n != 0:
        reversed_str += str(n % 10)
        n //= 10
    return sign + reversed_str


def reverse_integer_with_simple_code(n: int) -> str:
    """
    :param n: integer value
    :return: string
    """
    if not isinstance(n, int):
        raise TypeError("The parameter must be an integer.")
    return str(n)[::-1]


# Example usage
print(reverse_integer_with_simple_code(1110))  # Output: "0111"
print(reverse_integer_with_simple_code(54762))  # Output: "54321"
print(reverse_integer_with_simple_code(-10200))  # Output: "-00201"
