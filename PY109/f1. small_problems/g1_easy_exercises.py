## 1 Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def is_odd(my_int):
    try:
        if my_int % 2 != 0:
            return True
        elif my_int % 2 == 0:
            return False
    except TypeError:
        return 'wrong input, please enter an integer'

print(is_odd(3))
print(is_odd(100))
print(is_odd('test'))

# LS simpler solution:

def is_odd(number):
    return abs(number) % 2 == 1 #abs ins not required but transforms the integer to its absolute value (no negative)

## 2 Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# My solution using a list comprehension with a conditional

my_range = list(range(1,100))

[print(number) for number in my_range if number % 2 == 1]

# LS solution: simpler with for loop

for number in range(1,100, 2):
    print(number)

## 3 Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

for number in range(2, 99, 2):
    print(number)

## 4 Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet. # Note: 1 square meter == 10.7639 square feet

length = float(input('Enter the length of the room in meters: '))
width = float(input('Enter the width of the room in meters: '))

area_sqm = length * width
area_sqf = area_sqm * 10.7639

print(f"The area of the room is {area_sqm:.2f} square meters ({area_sqf:.2f} square feet).")
# :.2f format decimal to include only 2 decimals

## 5 Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the  concatenated_string amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

bill = float(input('What is the bill? '))
tip_perc = float(input('What is the tip percentage? '))

tip = bill * tip_perc / 100 concatenated_string = bill + tip

print(f"The tip is ${tip:.2f}\nThe  concatenated_string is $ concatenated_string:.2f}")

## 6 Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

my_integer = int(input('Please enter an integer greater than 0: '))
my_operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')
my_range = range(1, my_integer + 1)

def sum_or_product(choosen_operation):
    if choosen_operation == 's':
        result = 0
        for number in my_range:
            result += number
        return f"The sum of the integers between 1 and {my_integer} is {result}"
    elif choosen_operation == 'p':
        result = 1
        for number in my_range:
            result *= number
        return f"The product of the integers between 1 and {my_integer} is {result}"
    else:
        return 'incorrect input, enter "s" or "p"'

print(sum_or_product(my_operation))

## 7 Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

def short_long_short(string1, string2):
    if len(string1) > len(string2):
        concatenated_string = string2 + string1 + string2
    else:
        concatenated_string = string1 + string2 + string1
    return  concatenated_string

## 8 Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.

# For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

# To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0: # and year % 400 != 0 (no need to add this condition, it is implicit after passing previous condition)
        return False
    elif year % 4 == 0: # and year % 100 != 0 (no need to add this condition, it is implicit after passing previous condition)
        return True
    else:
        return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

## 9 Leap Years (Part 2)
# In the previous exercise, we assumed that the Gregorian calendar has been in continuous use since the year 1. However, the Gregorian calendar wasn't adopted until much later; prior to that, much of the world used the Julian calendar, which observed leap year every 4 years.

# in 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. Update the function from the previous exercise so it uses the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

def is_leap_year(year):
    if year < 1752 and year % 4 == 0:
        return True
    elif year < 1752: # and year % 4 != 0 (no need to add this condition, it is implicit after passing 1st condition)
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0: # and year % 400 != 0 (no need to add this condition, it is implicit after passing previous condition)
        return False
    elif year % 4 == 0: # and year % 100 != 0 (no need to add this condition, it is implicit after passing previous condition)
        return True
    else:
        return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

## 10 Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

def multisum(number):
    my_range = range(1, number +1)
    my_list = []

    for my_num in my_range:
        if my_num % 3 == 0 or my_num % 5 == 0:
            my_list.append(my_num)

    sum_total = sum(my_list)

    return sum_total

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

#LS improved version:
def multisum(number):
    sum_total = 0

    for my_num in range(1, number +1):
        if my_num % 3 == 0 or my_num % 5 == 0:
            sum_total += my_num

    return sum_total

#LS version using list comprehension:
def multisum(number):
    return sum([my_num for my_num in range(1, number +1) if my_num % 3 == 0 or my_num % 5 == 0])
# generator expression would be the same expression above but without the brackets []

##11 Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

def utf16_value(string):
    sum_utf16 = 0
    for char in string:
        utf16_value = ord(char)
        sum_utf16 += utf16_value
    return sum_utf16

# LS simplification (remove variable utf16_value)

def utf16_value(string):
    sum_utf16 = 0
    for char in string:
        sum_utf16 += ord(char)
    return sum_utf16

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
