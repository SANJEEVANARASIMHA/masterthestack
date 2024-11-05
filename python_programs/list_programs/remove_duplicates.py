n_list = [21, 52, 12, 45, 78, 12, 45, 78, 89, 84, 12]
n_list1 = [21, 52, 12, 45, 78, 12, 45, 78, 52, 52, 12]
n_list2 = [21, 52, 45, 45, 78, 12, 45, 78, 52, 52, 12]
n_list.remove(12)
print(n_list)


def remove_duplicates(n_list: list) -> list:
    for value in n_list:
        while value in n_list:
            if n_list.count(value) > 1:
                n_list.remove(value)
            else:
                break
    return n_list


def remove_duplicates_with_new_list(n_list: list) -> list:
    nn = []
    for value in n_list:
        if value not in nn:
            nn.append(value)
    return nn


def remove_duplicates_with_set(n: list) -> list:
    return list(set(n))


print(remove_duplicates(n_list))
print(remove_duplicates_with_set(n_list1))
print(remove_duplicates_with_new_list(n_list1))
