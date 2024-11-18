class Arthematic:

    def add(self, *args):
        if len(args) == 1:
            print(args)
        elif len(args) == 2:
            return sum(args)
        elif len(args) >= 5:
            for i in args:
                print(i * i)
        else:
            for i in args:
                print(i * 2)


cal_obj = Arthematic()
print(cal_obj.add(1, 10))  # 11
print(cal_obj.add(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 15
print(cal_obj.add(1, 2, 4))
print(cal_obj.add(1))

from functools import singledispatch


@singledispatch
def greet(arg):
    print("Hello!")


@greet.register
def _(arg: str):
    print(f"Hello, {arg}!")


@greet.register
def _(arg: int):
    print(f"You entered the number {arg}!")


# Example usage
greet("Alice")  # Hello, Alice! (overload for str)
greet(42)  # You entered the number 42! (overload for int)
greet(3.14)  # Hello! (default implementation)


class Test:

    def add(self, *args):
        if isinstance(args, int):
            return sum(args)
        else:
            return ["".join(i) for i in args if isinstance(i, str)]


test_obj = Test()
print(test_obj.add(1, 2, 3))
print(test_obj.add("hello", "world"))

print("****************************************************")


class test:

    def add(self, a, b):
        return a + b


test_obj = test()
print(test_obj.add(2, 4))
print(test_obj.add("hello", "world"))
