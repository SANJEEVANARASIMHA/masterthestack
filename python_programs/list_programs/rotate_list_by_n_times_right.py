n_list = [21, 52, 45, 78, 12]
n_list1 = [21, 52, 45, 78, 12]
n_list2 = [21, 52, 45, 78, 12]
n_list3 = [21, 52, 45, 78, 12]


def rotate_right(lst: list, k: int) -> list:
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


def rotate_right_with_out_in_built(lts: list, k: int) -> list:
    if not lts:
        return lts
    for _ in range(k):
        item = lts.pop(0)
        lts.append(item)
    return lts


def rotate_left_with_out_in_built(lts: list, k: int) -> list:
    if not lts:
        return lts
    for _ in range(k):
        item = lts.pop()
        lts.insert(0, item)
    return lts


def rotate_right(lst: list, k: int) -> list:
    if not lst or k == 0:
        return lst
    n = len(lst)
    k = k % n
    rotated_lst = [0] * n
    for i in range(n):
        new_position = (i + k) % n
        rotated_lst[new_position] = lst[i]
    return rotated_lst


print(rotate_right_with_out_in_built(n_list2, 2))
print(rotate_left_with_out_in_built(n_list3, 2))
print(rotate_right(n_list, 2))
