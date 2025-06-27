## 1 Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

def repeat(my_string, my_integer):
    if type(my_string) == str and type(my_integer) == int:
        my_range = range(my_integer)
        for number in my_range:
            print(my_string)
    else:
        print('Wrong input, introduce string and integer.')

repeat('Hello', 3) # Hello Hello Hello
repeat(3, 3) # Wrong input, introduce string and integer.

## improved code after LsBot suggestions:

def repeat(my_string, my_integer):
    if isinstance(my_string, str) and isinstance(my_integer, int): #isinstance instead of type()
        if my_integer <= 0:
            print ('Introduce an integer greater than 0.') # handling negative numbers
            return # finishing the loop
        for number in range(my_integer):
            print(my_string)

    else:
        print('Wrong input, introduce string and integer.')

## 2 Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

def crunch (my_string):
    new_string = ''
    for char in my_string:
        if len(new_string) == 0 or new_string[-1] != char:
            new_string += char
        else:
            continue
    return new_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

## improved code after LsBot suggestions:

def crunch (my_string):
    new_string = ''
    for char in my_string:
        if not new_string or new_string[-1] != char: # if not new string is more pythonic than if len(new_string) == 0
            new_string += char # no need for else: return, python will continue automatically
    return new_string

## 3 Write a function that takes a short line of text and prints it within a box.

def print_in_box(text):
    horizontal_rule = f'+-{"-" * len(text)}-+'
    empty_line = f'| {" " * len(text)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {text} |')
    print(empty_line)
    print(horizontal_rule)

print_in_box('To boldly go where no one has gone before.')

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

## 4 Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(number):
    binari_string = ''
    for binari in range(number):
        if binari % 2 == 0:
            binari_string += '1'
        elif binari % 2 == 1:
            binari_string += '0'
    return binari_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

## improved code after LsBot suggestions:

def stringy(number):
    result = ''
    for index in range(number):
        if index % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result

## 5 Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(n):
    for index in range(1,n + 1):
        print(f'{" " * (n - index)}{index * "*"}')

triangle(5)

#     *
#    **
#   ***
#  ****
# *****

## 6 Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.

noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
print(f"The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.")
print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")

## 7 A double number is an even-length number whose left-side digits are exactly the same as its right-side digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.

def twice(number):
    my_string = str(number)
    if my_string[:(len(my_string)//2)] == my_string[(len(my_string)//2):]:
        return number
    else:
        return(number * 2)

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

## improved code after LsBot suggestions:

def is_double_number(number): # new helper function
    string_number = str(number) # variable name amended for intent clearer
    center = len(string_number)//2 # new variable to simplify function
    return string_number[:center] == string_number[center:] # true when they are equal, false when they are not

def twice(number):
    if is_double_number(number):
        return number
    else:
        return(number * 2)

## 8 Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.
## Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

def get_grade(num1, num2, num3):
    score = (num1 + num2 + num3)/3
    match score:
        case score if 90 <= score <= 100:
            return 'A'
        case score if 80 <= score < 90:
            return 'B'
        case score if 70 <= score < 80:
            return 'C'
        case score if 60 <= score < 70:
            return 'D'
        case score if 0 <= score < 60:
            return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

## LS alternative using if/elif:

def get_grade(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3

    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

## 9 Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

def clean_up(my_string):
    new_string = ''
    for char in my_string:
        if char.isalpha():
            new_string += char
        elif not new_string or new_string[-1] != ' ': # most difficult line to think of
                new_string += ' '
    return new_string

print(clean_up("---what's my +*& line?") == " what s my line ") # True

## 10 Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.
#New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

def century(number):
    if str(number)[-1] == '0': #if str(number).endswith('0'): -> alternative with endswith instead of slice
        centure = str((number // 100))
        result = centure + 'th'
        return result
    else:
        centure = str((number // 100) + 1)
        if centure[-2:] == '11' or centure[-2:] == '12' or centure[-2:] == '13':
            result = centure + 'th'
        elif centure[-1] == '1':
            result = centure + 'st'
        elif centure[-1] == '2':
            result = centure + 'nd'
        elif centure[-1] == '3':
            result = centure + 'rd'
        else:
            result = centure + 'th'
        return result

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

#LS solution with two functions and matchcase.

def century(year):
    century_number = year // 100 + 1

    if year % 100 == 0:
        century_number -= 1

    suffix = century_suffix(century_number)
    return f'{century_number}{suffix}'

def century_suffix(century_number):
    last_two = century_number % 100
    last_digit = century_number % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'

    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'