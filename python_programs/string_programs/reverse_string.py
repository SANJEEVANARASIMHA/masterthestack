def reverse_string(s):
    return s[::-1]


string = "Hello, World!"
print(reverse_string(string))


def is_palindrome(s):
    s = s.lower()  # Convert to lowercase to handle case insensitivity
    return s == s[::-1]


# Example usage
string = "Madam"
print(is_palindrome(string))  # Output: True
