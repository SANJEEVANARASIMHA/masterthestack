# Input: n = 19
# Output: True
# 19 is Happy Number,
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# As we reached to 1, 19 is a Happy Number.
#
# Input: n = 20
# Output: False
def is_happy_number(n: int) -> bool:
    def get_next(number: int) -> int:
        return sum(int(digit) ** 2 for digit in str(number))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# Example usage
number = int(input("Enter a positive integer: "))
print(f"{number} is a happy number." if is_happy_number(number) else f"{number} is not a happy number.")
