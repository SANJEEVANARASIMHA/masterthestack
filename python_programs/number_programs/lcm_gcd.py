def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm(x: int, y: int) -> int:
    return abs(x * y) // gcd(x, y)


# Example usage
num1 = 12
num2 = 18
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
