n_list = [10, 5, 85, 96, 25, 41]


def get_max_min_with_in_built(n: list) -> tuple | str:
    if not len(n) >= 2:
        return "list length must be greater than 2"
    return min(n), max(n)


def get_max_min_with_sorted(n: list) -> tuple | str:
    if not len(n) >= 2:
        return "list length mujst be greater tgan 2"
    s_list = sorted(n)
    return s_list[0], s_list[-1]


def get_min_max_without_in_built(n: list) -> tuple | str:
    if not len(n) >= 2:
        return "list length must be greater than 2"
    min_v = max_v = n[0]
    for current in n:
        if current > max_v:
            max_v = current
        if current < min_v:
            min_v = current
    return min_v, max_v


print(get_max_min_with_in_built(n_list))
print(get_max_min_with_sorted(n_list))
print(get_min_max_without_in_built(n_list))

