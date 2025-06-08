# Lists

numbers = [1, 2, 3, 4, 5]

print(numbers)
print(len(numbers))

fruits = ["apple", "orange", "banana", "grape"]
print(fruits)

mixed_lists = [1, "Hello", 3.14, True]

print(mixed_lists)

my_list = [1, 2, 3, 4, 5]

print(my_list[0])
print(my_list[2])
print(my_list[-1])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

subset = my_list[2:6]
print(subset)

subset = my_list[5:]
print(subset)

subset = my_list[1:-1:2]
print(subset)

my_list = [1, 2, 3, 4, 5]
my_list[2] = 10

print(my_list)

my_list = [1, 2, 3, 4, 5]

del my_list[2]

my_list.remove(4)

print(my_list)

# Array

# 1D
my_list = [1, 2, 3, 4, 5]

# 2D
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(matrix[1][1])

# 3D
cube = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

print(cube)

print(cube[2][0][2])

# Array Function
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list.extend([5, 6, 7])
print(my_list)

my_list.insert(1, 21)
print(my_list)

popped_element = my_list.pop()
print(popped_element)
print(my_list)

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
my_list.sort()
print(my_list)

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)

# For Loop
my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

for number in range(3, 9):
    print(number)

for number in range(len(my_list)):
    print(number)

# While Loop

my_list = [1, 2, 3, 4, 5]
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1

# In Operator
text = "Hello, World!"
result = "o" in text
print(result)

# In SubStrings
sentence = "Python is powerful"
result = "power" in sentence
print(result)
