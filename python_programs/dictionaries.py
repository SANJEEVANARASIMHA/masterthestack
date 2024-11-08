# Write Python 3 code in this online editor and run it.
test_dict = {}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
test_dict.update(zip(keys, values))
print(test_dict)

# flatten dictiponary
#
nested_dict = {
    'a': 1,
    'b': {'b1': 2, 'b2': {'b21': 3, 'b22': 4}},
    'c': {'c1': 5}
}


# o_p = {
#     'a': 1,
#     'b_b1': 2,
#     'b_b2_b21': 3,
#     'b_b2_b22': 4,
#     'c_c1': 5
# }

def flatten_dict(nested_dict, dummy_key='', sep='_'):
    emp_dict = {}
    # dummy_key = ''
    for k, v in nested_dict.items():
        new_key = dummy_key + sep + k if dummy_key else k
        if isinstance(v, dict):
            emp_dict.update(flatten_dict(v, new_key, sep=sep))
        else:
            emp_dict.update({new_key: v})
    return emp_dict


res = flatten_dict(nested_dict)
print(res)

# flatten list:
in_list = [1, 2, [3, 4, 5, [7, 8, 9]]]


def flatten_list(in_list):
    # a_list = list(in_list)
    a_list = list(in_list)
    i = 0
    while i < len(a_list):
        if isinstance(a_list[i], list):
            a_list[i:i + 1] = a_list[i]
        else:
            i += 1
    return a_list


res = flatten_list(in_list)
print(res)

# update dict with default values if any key is missing
d = {'a': 1, 'b': 2, 'c': 3}
default = {'b': 4, 'e': 6}


def update_dict(d, default):
    for k, v in default.items():
        d.setdefault(k, v)
    return d


res = update_dict(d, default)
print(res)

lis = ['d', 'e', 'f']
for k in lis:
    if not k in d:
        d.setdefault(k, 0)
print(d)

# remove all items in dict having values as None
di = {'a': 1, 'b': None, 'c': 4, 'd': None}
keys = dict([(k, v) for k, v in di.items() if v is not None])
print(keys)

# find max val in dict find that key
di = {'a': 1, 'b': 6, 'c': 4, 'd': 9}
max_val = 0
max_key = 0
for k, v in di.items():
    if v > max_val:
        max_val = v
        max_key = k
print(max_key, max_val)

# find second max key and value pair
max_val = max(di.values())
second_max_val = 0
second_max_key = None
for k, v in di.items():
    if v != max_val:
        if v > second_max_val:
            second_max_val = v
            second_max_key = k
print(second_max_val, second_max_key)

unique_val = list(set(di.values()))
unique_val.sort()
s_m_v = unique_val[-2]
for k, v in di.items():
    if v == s_m_v:
        print(k)

# remove duplciate values in dict keeping only one occurance per value
di = {'a': 1, 'b': 1, 'c': 4, 'd': 9}
temp = {}
lis = []
for k, v in di.items():
    if v not in lis:
        lis.append(v)
        temp[k] = v
print(temp)

# get intersection of keys from two dictionaries. (get common key-value from two dict)
d1 = {'a': 1, 'b': 1, 'c': 4, 'd': 9}
d2 = {'d': 9, 'f': 10, 'g': 42, 'h': 19}

common_pairs = {}
for k in d1:
    if k in d2 and d1[k] == d2[k]:
        common_pairs[k] = d1[k]
print(common_pairs)

# merge two dictionaries
d1.update(d2)
print(d1)

# merge
merge_dict = d1 | d2
m_dict = {**d1, **d2}
print(m_dict)

# sum of all values in dict if all values are intergers
dic = {'a': 1, 'b': 1, 'c': 4, 'd': 9.0}
sum_res = sum([v for (k, v) in dic.items() if isinstance(v, int)])
print(sum_res)

# convert list of tuples into key-val pair
inp = [(1, 2), (4, 5), (7, 8)]
print(dict(inp))

# check if dict has specific nested key
nested_dict = {
    "a": {
        "b": {
            "c": 5
        }
    }
}
val = nested_dict['a']['b']['c']
print(val)

# Write a function to remove all key-value pairs where the key contains a specific substring
my_dict = {
    "username": "alice",
    "user_id": 123,
    "email": "alice@example.com",
    "age": 25
}
# {
#     "email": "alice@example.com",
#     "age": 25
# }
substring = "user"
res = {k: v for k, v in my_dict.items() if substring not in k}
print(res)

# handling missing keys without rasing error
# use get method
val = my_dict.get('rank', 69)
print(val)

## generator

# get consonants from string using generator

s1 = "SanjeevNarasimha"


def generator_function(s1):
    vowels = "aeiouAeiou"
    for char in s1:
        if char.isalnum() and char not in vowels:
            yield char


res = ''.join(generator_function(s1))
res1 = (*generator_function(s1),)
print(res)
print(res1)

list1 = [1, 2, 3, 4]
itr = iter(list1)
print(itr)
for i in itr:
    print(i)


# decorator
def logging_func(func):
    def inner(*args, **kwargs):
        print(f"args before func call  with {args} and {kwargs}")
        res = func(*args, **kwargs)
        print(f"after func call  and result is {res}")
        return res
    return inner

@logging_func
def sum(a, b):
    return a + b

sum(2,3)



import threading
import time

def numbers(start, end):
    for i in range(start, end):
        time.sleep(1)
        print(i)


def negative_num(start, end):
    for i in range(start, end):
        time.sleep(1.5)
        print(i)

thread1 = threading.Thread(target=numbers, args=(1,10))
thread2 = threading.Thread(target=negative_num, args= (-20, -10))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("threads are done")


class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    # def __str__(self):
    #     return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        print("a")
        return f'Ocean(\'{self.name}\', {self.age})'


c = Ocean('Jellyfish', 5)
# print(str(c))
print(c)
c = Ocean('Jellyfish', 7)
print(c)

# def res(add, a, b):
#     resl = add(a,b)
#     return resl

def add(a,b):
    return a+b

def sub(a, b):
    return a-b

res = [add, sub]
print(res[0](2,3))
print(res[1](4,2))

def print_name(x):
    print("printing : ", x)

a = print_name
print(a('123'))

import decimal

i = 10
res  = decimal.Decimal(i)
print(type(res))

# convert string of integers into decimal
x = "1234"
result = decimal.Decimal(x)
print(result)
print(x[::-1])

def count_vowels(a):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in a:
        if ch in vowels:
            count += 1
    return count
r = count_vowels("deepika")
print(r)

def occurance_char(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
a = "deepika"
occ_res = occurance_char(a)
print(occ_res)

def fibonacci(num):
    if num < 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

fib_res = fibonacci(10)
print(fib_res)

# max number
l = [1,8,2,5,3]
max_num = 0
for n in l:
    if n > max_num:
        max_num = n
print(max_num)

# middle element and convert list into string

l = [1,2,3,4,5]
ls = ["p", "y"]
mid_element = int(len(l)/2)
print(l[mid_element])
print(str(l))
print(''.join(str(i) for i in l))
st = ''.join(ls)
print(st)

