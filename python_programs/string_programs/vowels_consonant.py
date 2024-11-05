name = "sanjeevanarasimha"


def count_vowels_consonents(lts: str) -> dict:
    result = {"consonents": {}, "vowels": {}}
    for i in name:
        if i in ['a', 'e', 'i', 'o', 'u']:
            if i not in result['vowels'].keys():
                result['vowels'][i] = name.count(i)
        elif i not in result['consonents'].keys():
            result['consonents'][i] = name.count(i)
    return result


def count_vowels_consonents_without_builtin(lts: str) -> dict:
    result = {"consonents": {}, "vowels": {}}
    vowels = "aeiou"
    for i in name.casefold():
        if i.isalpha():
            if i in vowels:
                v_count = result['vowels'].get(i, 0) + 1
                result['vowels'][i] = v_count
                result['vowels']['total_count'] = result['vowels'].get('total_count', 0) + 1
            else:
                c_count = result['consonents'].get(i, 0) + 1
                result['consonents'][i] = c_count
                result['consonents']['total_count'] = result['consonents'].get('total_count', 0) + 1
    return result


print(count_vowels_consonents_without_builtin(name))
