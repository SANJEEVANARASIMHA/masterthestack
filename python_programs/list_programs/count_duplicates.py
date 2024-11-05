n_list = [21, 52, 12, 45, 78, 12, 45, 78, 89, 84, 12]
n_list1 = [21, 52, 12, 45, 78, 12, 45, 78, 52, 52, 12]
n_list2 = [21, 52, 45, 45, 78, 12, 45, 78, 52, 52, 12]


def count_duplicates(n: list) -> dict:
    dc = {}
    for i in n:
        if i in dc:
            dc[i] = dc[i] + 1
        else:
            dc[i] = 1
    return dc


def count_duplicates_with_in_built(n: list) -> dict:
    dc = {}
    for i in n:
        dc[i] = dc.get(i, 0) + 1
    return dc


def max_min_occurance(dc: dict) -> dict:
    max_count = 1
    min_count = 1
    max_item = None
    min_item = None

    for key, value in dc.items():
        if value >= max_count:
            max_item = key
            max_count = value
        if value <= min_count:
            min_count = value
            min_item = key
    return {max_item: max_count, min_item: min_count}


def max_min_occurance_with_in_built(dc: dict) -> dict:
    max_item = max(dc, key=dc.get)
    min_item = min(dc, key=dc.get)
    return {max_item: dc[max_item], min_item: dc[min_item]}


print(max_min_occurance(count_duplicates(n_list1)))
print(max_min_occurance_with_in_built(count_duplicates_with_in_built(n_list1)))
