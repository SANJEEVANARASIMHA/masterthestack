def common_characters(str1: str, str2: str) -> str:
    set1 = set(str1)
    set2 = set(str2)
    common_chars = set1.intersection(set2)
    return ''.join(sorted(common_chars))


string1 = "hello"
string2 = "world"
result = common_characters(string1, string2)
print(f"The common characters between '{string1}' and '{string2}' are: '{result}'")  # Output: 'lo'
