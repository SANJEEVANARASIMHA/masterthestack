name = "hello world"


def remove_duplciates(name: str) -> str:
    return "".join([i for i in set(name)])


print(remove_duplciates(name))
