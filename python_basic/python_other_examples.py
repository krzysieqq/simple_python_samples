import this
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Union:
print(A | B)  # Output: {1, 2, 3, 4, 5, 6}
# Intersection:
print(A & B)  # Output: {3, 4}
# Difference:
print(A - B)  # Output: {1, 2}
# Symmetric Difference:
print(A ^ B)  # Output: {1, 2, 5, 6}

# -- Arithmetic Operators --
A = 10
B = 20
# Addition
print(A + B)  # Output: 30
# Subtraction
print(A - B)  # Output: -10
# Multiplication
print(A * B)  # Output: 200
# Division
print(A / B)  # Output: 0.5
# Modulus
print(A % B)  # Output: 10
# Exponent
print(A ** B)  # Output: 100000000000000000000

# -- Comparison Operators --
a = 21
b = 10

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: True
print(a < b)  # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# -- Bitwise Operators --
a = 58  # 111010
b = 13  # 1101
# AND
print(a & b)  # Output: 8 = 1000
# OR
print(a | b)  # Output: 63 = 111111
# XOR
print(a ^ b)  # Output: 55 = 110111
# Left Shift
print(a << 2)  # Output: 232 = 11101000
# Right Shift
print(a >> 2)  # Output: 14 = 1110
