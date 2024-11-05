def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(n: int) -> list:
    return [fibonacci(i) for i in range(n)]


def fibonacci_sequence(n: int) -> list:
    fib_series = [0, 1]
    [fib_series.append(fib_series[-1] + fib_series[-2]) for _ in range(2, n)]
    return fib_series


# Example usage
number = int(input("Enter a positive integer: "))
# Example usage
print(fibonacci_series(number))
print(fibonacci_sequence(number))
