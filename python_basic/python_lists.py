list_example = ['Hi', 'I', 'am', 'list']
print(list_example)  # Output: ['Hi', 'I', 'am', 'list']
print(list_example[0])  # Output: Hi
print(list_example[0:2])  # Output: ['Hi', 'I']
print(list_example[2:4:2])  # Output: ['am']
# list_example[<start>:<end>:<step>]
print(list_example[::-1])  # Output: ['list', 'am', 'I', 'Hi']
list_example[2] = 'not'
print(list_example)  # Output: ['Hi', 'I', 'not', 'list']
del list_example[2]
print(list_example)  # Output: ['Hi', 'I', 'list']
print(len(list_example))  # Output: 3
print(list_example * 2)  # Output: ['Hi', 'I', 'list', 'Hi', 'I', 'list']

squares = []
for x in range(10):
    squares.append(x**2)
# It's the same
squares = list(map(lambda x: x**2, range(10)))
# or, equivalently to:
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)  # Output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# new_list = [expression(i) for i in old_list if filter(i)]
