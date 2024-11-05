def find_unique_elements(lst):
    counts = {}
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    unique_elements = [element for element, count in counts.items() if count == 1]
    return unique_elements


from collections import Counter


def find_unique_elements_by_using_in_built(lst):
    counts = Counter(lst)  # Create a Counter object
    return [element for element, count in counts.items() if count == 1]


example_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(find_unique_elements_by_using_in_built(example_list))
print(find_unique_elements(example_list))
