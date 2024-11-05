def decimal_to_binary(n: int) -> str:
    binary = ''
    if n == 0:
        return '0'
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def decimal_to_binary_with_in_built(n: int) -> str:
    return bin(n)[2:]  # Remove the '0b' prefix


# Example usage
number = 10
print(f"The binary representation of {number} is: {decimal_to_binary(number)}")

# Example usage
number = 10
print(f"The binary representation of {number} is: {decimal_to_binary_with_in_built(number)}")
