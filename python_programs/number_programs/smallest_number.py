def find_smallest(a: int, b: int, c: int) -> int:
    return a if a < b and a < c else (b if b < c else c)


def find_greatest(a: int, b: int, c: int) -> int:
    return a if a > b and a > c else (b if b > c else c)


def find_smallest_with_in_built(a: int, b: int, c: int) -> int:
    return min(a, b, c)


def find_greatest_with_in_built(a: int, b: int, c: int) -> int:
    return max(a, b, c)


print(find_smallest_with_in_built(3, 5, 3))
print(find_greatest_with_in_built(3, 5, 10))
