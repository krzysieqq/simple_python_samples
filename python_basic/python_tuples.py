tuple_example = (1, 2, 3, [4, ], 5)
print(tuple_example)  # Output: (1, 2, 3, [4], 5)
tuple_example[3].append(7)
print(tuple_example)  # Output: (1, 2, 3, [4, 7], 5)

