def remove_keys_from_dict():
    """
    If the key doesn’t exist, pop() will return None (or another default value if specified),
    and the dictionary remains unchanged.
    :return:
    """
    data = {'apple': 2, 'banana': 3, 'cherry': 5}
    key_to_remove = 'banana'
    removed_value = data.pop(key_to_remove, None)
    print("Updated Dictionary:", data)
    print("Removed Value:", removed_value)


remove_keys_from_dict()
