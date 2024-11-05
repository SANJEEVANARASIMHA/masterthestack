def is_pangram(s: str) -> bool:
    """A pangram is a sentence that contains every letter of the alphabet at least once.
     To check if two strings are pangrams,
     you can create a function that verifies whether each string contains all 26 letters of the English
    alphabet."""
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    input_set = set(char for char in s if char.isalpha())
    return alphabet <= input_set


def check_pangrams(str1: str, str2: str) -> (bool, bool):
    return is_pangram(str1), is_pangram(str2)


# Example usage
string1 = "The quick brown fox jumps over the lazy dog"
string2 = "This is not a pangram"

result1, result2 = check_pangrams(string1, string2)

if result1:
    print(f'"{string1}" is a pangram.')
else:
    print(f'"{string1}" is not a pangram.')

if result2:
    print(f'"{string2}" is a pangram.')
else:
    print(f'"{string2}" is not a pangram.')
