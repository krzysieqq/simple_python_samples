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
