def split_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
split_into_chunks(example_list, 2)
