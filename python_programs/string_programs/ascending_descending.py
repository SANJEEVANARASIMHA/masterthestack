def sort_string(s: str):
    ascending = ''.join(sorted(s))
    descending = ''.join(sorted(s, reverse=True))
    return ascending, descending


# Example usage
input_string = "python"
ascending_order, descending_order = sort_string(input_string)

print("Ascending Order:", ascending_order)  # Output: "hnopty"
print("Descending Order:", descending_order)  # Output: "ytphon"
