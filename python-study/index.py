# print value

print('Hello World ')

# define variable
age = 20

age = "Hello"

# print with variable
print("My age is:", age)

# Case Sensitivity
password = 12345
Password = 54321
print(password)
print(Password)

number1 = 8
number2 = 3

# Arithmetic
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 // number2)
print(number1 % number2)
print(number1 ** number2)

# Input Function
user_input = input("Enter something: ")
print("You entered", user_input)

# Assignment Operators
x = 10
x += 5
print(x)
y = 20
y -= 3
print(y)
z = 5
z *= 2
print(z)

# Strings
my_name = "My name is Hieu"

multiline_string = """This is a 
multiline
string.
"""

print(my_name)
print(multiline_string)

# Concatenation
str1 = "Hello"
str2 = "World"

concatenated_string = str1 + " " + str2
print(concatenated_string)

# String length
string_len = "Python"
my_length = len(string_len)
print(my_length)

# String Indexing and Slicing
text = "Python"
first_char = text[0]
print(first_char)
substring = text[1:4]
print(substring)

# String Formatting
name = "Hello World"
age = 40

formatted_string = f"My name is {name} and I am {age} years old"
print(formatted_string)

# Escape Characters
escaped_string = "This is a line.\n This is a new line"
print(escaped_string)

# Booleans
is_male = True
print(is_male)

# Check Type
print(type(is_male))
my_num = 20.10
print(type(my_num))

# Type Casting
float_num = 3.14
int_num = int(float_num)
print(type(float_num))
print(type(int_num))

num_int = 5
num_float = float(num_int)
print(num_float)
print(type(num_float))

num = 20
str_num = str(num)
print(type(str_num))
print(str_num)

num = 1
bool_value = bool(num)
print(bool_value)

# String Methods
text = "Hello, World!"
upper_text = text.upper()
lower_text= text.lower()
print(upper_text)
print(lower_text)

phrase = "python programming is fun!"
cap_phrase = phrase.capitalize()
print(cap_phrase)
title_phrase = phrase.title()
print(title_phrase)

sentence ="            Python is fun!            "
stripped_sentence = sentence.strip()
print(sentence)
print(stripped_sentence)
lstripped_sentence = sentence.lstrip()
print(lstripped_sentence)
rstripped_sentence = sentence.rstrip()
print(rstripped_sentence)

filename = "example.text"
starts_with = filename.startswith("example")
print(starts_with)
ends_with = filename.endswith(".text")
print(ends_with)

sentence = "I like programming in Java."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)

phrase = "Python is powerful and Python is easy to learn"
index1 = phrase.find("Python")
index2 = phrase.index("Python")
print(index1)
print(index2)

sentence = "Python is a powerful programming language"
words = sentence.split(" ")
print(words)

sentence = "Python is easy. Python is fun. Python is powerful"
count_python = sentence.count("Python")
print(count_python)

# Comparison Operators
a = 5
b = 10

result = a == b
print(result)
result = a != b
print(result)
result = a > b
print(result)

# Logical Operators
print(True and True)
print(True & False)
print(False or False)
print(True | False)
print(not True)
x = True
y = False
result = x and y
print(result)
result = x or y
print(result)
result = not y
print(result)

# Conditional Statement

x = 2

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

password = 8

if password > 8:
    print("Valid password")
elif password < 8:
    print("Invalid password")
else:
    print("Please enter your password to login")

# For Loops

for index in range(5):
    print(index)

for index in range(1, 10):
    print(index)

for index in range(1, 10, 2):
    print(index)

word = "Python"

for char in word:
    print(char)

for char in word:
    print(char.split(" "))

# While Loops

password = ""

while len(password) < 8:
    password = input("Enter a password at least 8 characters")
print("Change Password Successfully")

# Example - Menu-Drive Program

choice = None

while choice != "q":
    print("1. Option 1")

    print("2. Option 2")

    print("3. Option 3")

    choice = input("Enter your choice (or 'q' to quit): ")

