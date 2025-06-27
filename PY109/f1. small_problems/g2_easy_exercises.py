#### 1 Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

def greetings(name_parts,info):
    full_name = " ".join(name_parts)
    tittle = info["title"]
    occupation = info["occupation"]

    output = f"Hello, {full_name}! Nice to have a {tittle} {occupation} around."
    return output

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

#### This problem was hard to solved. Important to remember that function parameters in Python cannot contain lists or dictionary symbols and need to be splitted in parts.

## 2 Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase)

user_name = input('What is your name? ')
if user_name.endswith('!'):
    print(f'HELLO {user_name.upper()}! WHY ARE WE YELLING?')
else:
    print(f'Hello {user_name}.')

# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

## 3 Create a function that takes two arguments, multiplies them together, and returns the result.

def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 3) == 15)  # True

## 4 Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

def square(num1):
    return multiply(num1, num1)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

## 5 Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

def prompt(text):
    return input(f'==> {text} ')

def result(text):
    print(f'==> {text}')

num1 = float(prompt('Enter the first number: '))
num2 = float(prompt('Enter the second number: '))

addition = num1 + num2
subtraction = num1 - num2
product = num1 * num2
quotient = num1 / num2
floor_quotient = num1 // num2
remainder = num1 % num2
power = num1 ** num2

result(f'{num1} + {num2}  = {addition:.2f}')
result(f'{num1} - {num2}  = {subtraction:.2f}')
result(f'{num1} * {num2}  = {product:.2f}')
result(f'{num1} / {num2}  = {quotient:.2f}')
result(f'{num1} // {num2}  = {floor_quotient:.2f}')
result(f'{num1} % {num2}  = {remainder:.2f}')
result(f'{num1} ** {num2}  = {power:.2f}')


# ==> Enter the first number:
# 3.141592
# ==> Enter the second number:
# 2.718282
# ==> 3.141592 + 2.718282 = 5.859811
# ==> 3.141592 - 2.718282 = 0.42324699999999993
# ==> 3.141592 * 2.718282 = 8.539561733178
# ==> 3.141592 / 2.718282 = 1.1557038600115808
# ==> 3.141592 // 2.718282 = 1.0
# ==> 3.141592 % 2.718282 = 0.42324699999999993
# ==> 3.141592 ** 2.718282 = 22.45792517468373

## 6 Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

def penultimate(string):
    word_list = string.split()
    return word_list[-2]


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

## 7 In this exercise, you will write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

def xor(value1, value2):
    if value1 and value2:
        return False
    elif value1 or value2:
        return True
    else: # no need for else clause, at this point both
        return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

## 8 Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

#using a loop and a range
def oddities(my_list):
    odd_list = []
    for index in range(0, len(my_list), 2):
        odd_list.append(my_list[index])
    return odd_list

# using slice (cleaner solution)
def oddities(my_list):
    odd_list = my_list[::2]
    return odd_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

## 9 Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

import random

teddy_age = random.randint(20, 100)
print(f'Teddy is {teddy_age} years old!')

# Important note, since randint includes both endpoints, we should use random.randint(20, 100) instead of (20,101) to stay within the specified range of 20 to 100.

## 10 Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))
current_year = datetime.now().year
retirement_year = current_year + retirement_age - age
years_left = retirement_age - age

print(f"It's {current_year}. You will retire in {retirement_year} ")
print(f"You have only {years_left} years of work to go!")

#### 11 Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

def center_of(text):
    mid = len(text) // 2
    if len(text) % 2 == 0:
        return text[mid - 1:mid + 1]
    else:
        return text[mid]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True

#### I ended up doing this exercise right, but I needed some help reminding me to use the slice to access the middle 2 characters of the string, and that the last character is -1

## 12 Write a function that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the argument is a negative number, return it as-is.

def negative(number):
    if number > 0:
        return -number
    return number

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
