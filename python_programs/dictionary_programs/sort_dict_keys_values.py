data = {'hello': 5, 'banana': 1, 'cherry': 2, 'date': 8}


def sort_dict(data: dict) -> dict:
    return dict(sorted(data.items(), key=lambda item: item[0]))


def sort_dict_by_keys(data: dict) -> dict:
    keys = list(data.keys())
    values = list(data.values())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[j] < keys[i]:
                keys[j], keys[i] = keys[i], keys[j]
                values[j], values[i] = values[i], values[j]

    sorted_dict = {keys[i]: values[i] for i in range(len(keys))}
    return sorted_dict


def sort_dict_by_values(data: dict) -> dict:
    keys = list(data.keys())
    values = list(data.values())
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] < values[i]:
                keys[j], keys[i] = keys[i], keys[j]
                values[j], values[i] = values[i], values[j]

    sorted_dict = {keys[i]: values[i] for i in range(len(keys))}
    return sorted_dict


print(sort_dict(data))
print(sort_dict_by_keys(data))
print(sort_dict_by_values(data))
