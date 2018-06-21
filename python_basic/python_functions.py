# Enforcing Named Parameters


# We can use * to force a user to supply named arguments:
def fn(*, a=100, b=200):
    return a + b * 10


print(fn())  # Output: 2100
print(fn(b=30, a=10))  # Output: 310
# print(fn(10, 20))  # TypeError fn() takes 0 positional arguments but 2 were given


# Variadic functions have a variable number of parameters. They can be collected into a tuple with a * prefix
def fn(a, *items):
    result = 0
    for item in items:
        result += item
    return a + result


print(fn(10))  # 10
print(fn(10, 20))  # 30
print(fn(10, 20, 30, 40, 50))  # 150


# Decorators
# Simple Python Cache Decorator
def simple_cache(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
        return rv
    return wrapper


class Memorize(dict):
    def __init__(self, func):
        super(Memorize, self).__init__()
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


@simple_cache
def f(value):
    print('Hi I`m f with {}'.format(value))
    return value * 2


@simple_cache
def g(value):
    print('Hi I`m g with {}'.format(value))
    return value * 3


print(f(2))  # Hi I`m f with 2 -> Output: 4
print(g(2))  # Hi I`m g with 2 -> Output: 6
print(f(3))  # Hi I`m f with 3 -> Output: 6
print(g(3))  # Hi I`m g with 3 -> Output: 9
print(f(2))  # Output: 4
print(g(2))  # Output: 6


@simple_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


def fn(a=100, b=200):
    return a + b


print(fn())  # 100 + 200
print(fn(10))  # 10 + 200
print(fn(10, 20))  # 10 + 20


def fn(a, *all):
    sum = 0
    for item in all:
        sum += item
    return a + sum


print(fn(10))  # 10
print(fn(10, 20))  # 30
print(fn(10, 20, 30, 40, 50))  # 150


def fn(**kwargs):
    return kwargs['a'] + kwargs['b']


print(fn(a=200, b=500))  # 700

d1 = {'a': 100, 'b': 200}
print(fn(**d1))  # 300

num = 9


def f1():
    num = 20


def f2():
    print(num)


f2()  # 9
f1()
f2()  # 9

b = 3


def f1():
    b = 10

    def f2():
        nonlocal b  # global b
        if b < 100:
            b += 1

    f2()
    print(b, "from f1")


f1()
print(b, "from main")


def getmulby(m):
    def op(n):
        return m * n

    return op


f1 = getmulby(10)
f2 = getmulby(5)

print(f1(2))  # 20
print(f2(2))  # 10


def add_stars(some_function):
    def wrapper():
        print("********************")
        some_function()
        print("********************")

    return wrapper


@add_stars
def my_function():
    print("Hello!!!")


my_function()

ls = [2, 4, 6]

newlist = map(lambda item: item * 2, ls)

for n in newlist:
    print(n)

import random

f1 = lambda x: x + 10
f2 = lambda: random.randint(100, 200)
f3 = lambda x, y: x + y
compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)

print(f1(10))  # 20
print(f2())  # prints random number
print(f3(2, 3))  # 5
print(compare(10, 20))  # -1


def add(a, b):
    """ Simple function - add 2 numbers"""
    return a + b

# >>> help(add)
# Help on function add in module __main__:
# add(a, b)
#     Simple function - add 2 numbers


def add(a: "first number" = 0,
        b: "second number" = 0) -> "sum of a and b":
    return a + b


for item in add.__annotations__.items():
    print(item)

# ('a', 'first number')
# ('b', 'second number')
# ('return', 'sum of a and b')
