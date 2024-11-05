from typing import List


def find_sec_largets_with_sorted(n: list) -> int | str:
    if len(n) < 2:
        return "list length must greater than or equal to 2"
    return sorted(set(n))[-2]


def find_sec_largest_with_max(n: list) -> int | str:
    if len(n) < 2:
        return "list length must greater than or equal to 2"
    max_value = max(n)
    n.remove(max_value)
    return max(n)


def find_second_largest(numbers: list) -> int | str:
    if len(numbers) < 2:
        return "list length must greater than or equal to 2"

    largest = second_largest = 0
    for current in numbers:
        if current > largest:
            second_largest = largest
            largest = current
        elif current > second_largest != 0:
            second_largest = current
    return second_largest


nums = [5, 6, 8, 7, 5, 9, 4]
print(find_sec_largets_with_sorted(nums))
print(find_sec_largest_with_max(nums))
print(find_second_largest(nums))
