list1 = [2, 0, 2, 1, 1, 0]


def sort_zeros_and_ones(list1: list) -> list:
    for i in range(len(list1)):
        max_id = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[max_id]:
                max_id = j
        if max_id != i:
            list1[max_id], list1[i] = list1[i], list1[max_id]
    return list1


print(sort_zeros_and_ones(list1))
