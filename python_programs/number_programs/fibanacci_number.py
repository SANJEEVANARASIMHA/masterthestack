from typing import List, Any


def fibanacci_number(n: int) -> List[int | Any]:
    a, b = (0, 1)
    series = [a]
    for _ in range(2, n):
        a, b = b, a + b
        series.append(a)
    return series


print(fibanacci_number(10))

d = "deepika"
print(list(d))

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merging dictionaries using |
merged_dict = dict1 | dict2
zipped = zip(dict1, dict2)
print(zipped)
for k, v in zipped:
    print(k, v)
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
