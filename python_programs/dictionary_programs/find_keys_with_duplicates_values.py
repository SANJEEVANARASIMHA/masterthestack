data = {'apple': 2, 'banana': 3, 'cherry': 5, "organe": 3, "gua": 3}


def find_keys_from_duplicate_values(data: dict) -> list:
    value_to_keys = []
    for key, value in data.items():
        if list(data.values()).count(value) > 1:
            value_to_keys.append(key)
    return value_to_keys


print(find_keys_from_duplicate_values(data))


def find_keys_with_duplicate_values(d):
    value_to_keys = {}
    for key, value in d.items():
        if value in value_to_keys:
            value_to_keys[value].append(key)
        else:
            value_to_keys[value] = [key]
    duplicate_keys = {value: keys for value, keys in value_to_keys.items() if len(keys) > 1}
    return duplicate_keys


# Example usage
data = {'apple': 2, 'banana': 3, 'cherry': 2, 'date': 4, 'elderberry': 3}
result = find_keys_with_duplicate_values(data)
print("Keys with duplicate values:", result)
