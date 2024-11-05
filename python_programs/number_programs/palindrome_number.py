def is_palindrome(n: int) -> bool:
    original = n
    reversed_num = 0
    while n > 0:
        last_digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + last_digit  # Build the reversed number
        n //= 10  # Remove the last digit from n
    return original == reversed_num


n = 121
print(is_palindrome(n))
# a way by using a string Example usage
number = 121  # Change this number to test other cases
num_str = str(number)[::-1]
str_num = int(num_str)
print("palindrome" if number == str_num else "not palidorme")
