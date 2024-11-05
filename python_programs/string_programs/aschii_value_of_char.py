def ascii_values(s: str) -> list:
    return [(char, ord(char)) for char in s]

# Example usage
input_string = "hello"
ascii_list = ascii_values(input_string)

# Display the results
for char, ascii_val in ascii_list:
    print(f"Character: {char}, ASCII Value: {ascii_val}")
