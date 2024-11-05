def is_digit_or_special(s: str) -> bool:
    for char in s:
        if not (char.isdigit() or not char.isalnum()):  # Check if the character is not a digit and not alphanumeric
            return False  # If it’s a letter, return False
    return True  # Return True if all characters are digits or special characters

# Example usage
input_string = "12345!@#"
if is_digit_or_special(input_string):
    print(f'The string "{input_string}" contains only digits or special characters.')
else:
    print(f'The string "{input_string}" contains letters or other invalid characters.')
