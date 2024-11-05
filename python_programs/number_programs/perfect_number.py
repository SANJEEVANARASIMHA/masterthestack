# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# The smallest perfect number is 6, which has divisors 1, 2, and 3 (1 + 2 + 3 = 6).
def is_perfect_number(n: int) -> bool:
    if n < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n


def is_perfect_simple_code(n: int) -> bool:
    return True if n == sum([i for i in range(1, n) if n % i == 0]) else False


# Example usage
number = int(input("Enter a positive integer: "))
if is_perfect_simple_code(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
