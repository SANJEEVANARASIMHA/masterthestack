from typing import List

n_list = [10, 4, 52, 36, 85, 9]
n_list_1 = [10, 5, 52, 36, 85, 9]
n_list_2 = [10, 5, 52, 36, 5, 9]


def reverse_list_with_sclicing(n: list) -> list:
    return n[::-1]


def reverse_list_with_reverse(n: list) -> list:
    n.reverse()
    return n


def reverse_list(n: list) -> List:
    mid_len = int(len(n) / 2)
    for i in range(1, mid_len):
        if i < mid_len:
            temp = n[len(n) - i]
            n[len(n) - i] = n[i - 1]
            n[i - 1] = temp
    return n


print(reverse_list(n_list))
print(reverse_list_with_sclicing(n_list_1))
print(reverse_list_with_reverse(n_list_2))
