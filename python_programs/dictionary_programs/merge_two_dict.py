dict1 = {'apple': 2, 'banana': 3, 'cherry': 1}
dict2 = {'banana': 4, 'cherry': 5, 'date': 7}
dict3 = {'apple': 2, 'banana': 3, 'cherry': 1, "gua":1}
dict4 = {'banana': 4, 'cherry': 5, 'date': 7, "gua":2}


def merge_two_dict(dict1: dict, dict2: dict) -> dict:
    common_dict = dict1.copy()
    for key, value in dict2.items():
        if key in common_dict.keys():
            common_dict[key] = common_dict[key] + dict2[key]
        else:
            common_dict[key] = dict2[key]
    return common_dict


def merge_two_dict_compreshion(dict1: dict, dict2: dict) -> dict:
    merged_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in dict1.keys() | dict2.keys()}
    return merged_dict


merged_dict = dict1 | dict2
print("Merged Dictionary:", merged_dict)

print(merge_two_dict(dict1, dict2))
print(merge_two_dict_compreshion(dict3, dict4))

