list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

list3 = [1, 3, 5, 7]
list4 = [2, 4, 6, 8]


def merge_ascending_sorted_list(lts1: list, lts2: list) -> list:
    list1.extend(lts2)
    print(len(lts1))
    for i in range(len(lts1)):
        max_index = i
        for j in range(i + 1, len(lts1)):
            if list1[i] < list1[j]:
                max_index = j
        if max_index != i:
            list1[i], list1[max_index] = list1[max_index], list1[i]
    return lts1


def merge_descending_sorted_list(lts3: list, lts4: list) -> list:
    list3.extend(lts4)
    print(len(list3))
    for i in range(len(list3)):
        max_index = i
        for j in range(i + 1, len(list3)):
            if list1[i] > list1[j]:
                max_index = j
        if max_index != i:
            list1[max_index], list1[i] = list1[i], list1[max_index]
    return list3


print(merge_ascending_sorted_list(list1, list2))
print(merge_descending_sorted_list(list3, list4))
