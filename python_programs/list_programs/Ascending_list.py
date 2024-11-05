n_list = [21, 52, 12, 45, 78, 12, 45, 78, 89, 84, 12]


def ascending_list_with_sorted(n: list) -> list:
    return sorted(n)


def ascending_list(n: list) -> list:
    for i in range(len(n)):
        max_id = i
        for j in range(i + 1, len(n)):
            if n[j] < n[max_id]:
                max_id = j
        if max_id != i:
            n[i], n[max_id] = n[max_id], n[i]
    return n


print(ascending_list_with_sorted(n_list))
print(ascending_list(n_list))
