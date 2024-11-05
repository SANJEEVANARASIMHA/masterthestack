def leap_year(n: int) -> int:
    return (n % 4 == 0 and n % 100 != 0) or n % 400 == 0


print(leap_year(2024))
print(leap_year(1900))
print(leap_year(2020))

