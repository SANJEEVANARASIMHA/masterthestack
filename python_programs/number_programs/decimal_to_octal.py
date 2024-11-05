def decimal_to_octal_with_in_built(n: int) -> str:
    return oct(n)[2:]  # Remove the '0o' prefix


def decimal_to_octal(n: int) -> str:
    if n == 0:
        return '0'
    octal = ''
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal


# Example usage
number = 10
print(f"The octal representation of {number} is: {decimal_to_octal(number)}")

print(f"The octal representation of {number} is: {decimal_to_octal_with_in_built(number)}")
