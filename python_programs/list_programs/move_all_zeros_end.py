def move_zeroes_to_end_with_in_built(lst: list) -> list:
    non_zero_elements = [x for x in lst if x != 0]
    zero_count = lst.count(0)
    return non_zero_elements + [0] * zero_count


def move_zeros_to_end(lst: list) -> list:
    max_index = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            if i != max_index:
                lst[max_index], lst[i] = lst[i], lst[max_index]
            max_index = max_index + 1
    return lst


# Example usage
example_list = [0, 1, 0, 3, 12]
example_list1 = [0, 1, 0, 3, 12]
print(move_zeros_to_end(example_list))
print(move_zeroes_to_end_with_in_built(example_list1))
