def common_elements_set(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


# Example usage
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common = common_elements_set(list_a, list_b)
print(common)  # Output: [3, 4, 5]
