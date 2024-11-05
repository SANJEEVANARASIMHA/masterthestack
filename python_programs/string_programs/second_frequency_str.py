def second_most_frequent_char(s: str) -> str:
    char_count = {}
    for char in s:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    print(sorted_chars)
    if len(sorted_chars) < 2:
        return "Not enough unique characters"
    return sorted_chars[1][0]


input_string = "character"
result = second_most_frequent_char(input_string)
print(f"The second most frequent character in '{input_string}' is: '{result}'")
