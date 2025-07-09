## 1: What does this return and why? What concept does this cover?

def convert_to_int(string):
    try:
        converted_integer = int(string)
        return converted_integer
    except ValueError:
        return "That string cannot be converted to an integer"

print(convert_to_int("hello"))

print(convert_to_int("5"))

# In this first exercise, we define the function convert_to_int which takes a single parameter called string. Inside the function, we use a try and except block. The try block attempts to convert the input value to an integer using the int() constructor. If successful, it returns the converted integer. If the conversion fails and raises a ValueError (because the input is not a valid numeric string), the except block returns a message saying the string cannot be converted. When we call convert_to_int("hello"), Python raises a ValueError since "hello" cannot be converted to an integer, and the function returns the error message. In the second call, convert_to_int("5"), the string "5" is successfully converted to the integer 5, and that value is returned and printed.

# This example demonstrates explicit coercion, where we intentionally convert a string to an integer using the int() constructor. And implicit coercion, with print function which converts the integer 5 back into a string "5", for output.

## 2: What does this return and why? What concept does this cover?

def division(number1, number2):
    numerator = number1
    denominator = number2

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "The denominator cannot be zero"

print(division(5, 0))

# Explanation: In this example, we define the function division with two parameters: number1 and number2. We assign number1 to the variable numerator and number2 to denominator. Inside a try block, we attempt to divide the numerator by the denominator and return the result. However, if the denominator is zero, Python will raise a ZeroDivisionError. In that case, the except block will catch the error and return a message saying "The denominator cannot be zero," preventing the program from crashing. This is exactly what happens when we call division(5, 0) — since dividing by zero is not allowed, the function returns the custom error message.
# The concept explained here is the try and except blocks, and how the except block avoids Python from raising and error and crashing.

## 3: What does this return and why? What concept does this cover?

def addition(number1, number2):
    number1 += number2

x = 1
y = 2

addition(x, y)
print(f"x is {x}, y is {y}")

# x is 1, y is 2 (global variables untouched)
# Explanation: In this example, we define two global variables, x = 1 and y = 2. Then we define a function called addition that takes two parameters: number1 and number2. Inside the function, we use an augmented assignment: number1 += number2. When we call addition(x, y), the values of x and y — which are both integers — are passed into the function. However, since integers are immutable in Python, the operation number1 += number2 does not modify the original object. Instead, it creates a new integer object and assigns it to the local variable number1, which has no effect on the global variable x. As a result, when we print x and y after the function call, they still hold their original values: x is 1, and y is 2. This demonstrates that operations on immutable types like integers inside a function do not change the original variables outside the function.

## 4: What does this print and why? What concept does this cover? How would you refactor this to remove the space?
print(2 + 3 * 4, 4 * (3 + 2))

# 15 20
# In this example, we perform arithmetic operations that demonstrate operator precedence in Python. Multiplication has higher precedence than addition, so in the first expression 2 + 3 * 4, the multiplication happens first: 3 * 4 = 12, followed by the addition: 2 + 12 = 14. In the second expression, 4 * (3 + 2), the parentheses take precedence and force the addition to happen first: 3 + 2 = 5, and then 4 * 5 = 20. The use of a comma inside the print() function allows us to print both results side by side. So the final output is: 14 20. This example highlights the importance of operator precedence and how parentheses can be used to override it.

## 5: What can be used in place of commas to make this more readable?

print(123112940)

# Underscore can replace commas print(123_112_940)