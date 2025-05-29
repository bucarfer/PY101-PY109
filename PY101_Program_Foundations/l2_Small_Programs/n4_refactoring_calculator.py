'''
Part 2, Refactoring Calculator
Command line calculator program:
-Ask the user for two numbers.
-Ask for the operation: add, subtract, multiply or divide.
-Perform the calculation and display the result'''

#Part 3-2. Importing messages to the file from a JSON configuration file
import json

###REVISED. invalid nan
import math

#Load the messages from the JSON file
with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)
###REVISED. encoding UTF-8 parameter added, modern encoding that supports all languages and symbols.

#Part 3-4. Ask the user for language choice:
lang_choice = input("choose language/elige lenguaje (en/es): ").strip().lower()
if lang_choice not in ['en', 'es']:
    print("Invalid choice. English by default. \n opcion invalida. Ingles seleccionado")
    LANGUAGE = 'en'
else:
    LANGUAGE = lang_choice

#Part 3-3. Function to get translation
def translate(message, lang=LANGUAGE):
    """translate message to different languages"""
    return MESSAGES[lang][message]

# new print function to add message before each line
def prompt(message):
    """display message to user with prefix"""
    message = translate(message, lang=LANGUAGE) # Part 3-3
    print(f'=> {message}')

# check if number1 is valid
def invalid_number(number_str):
    """returns True if input cannot be converted to a float"""
    try:
        num = float(number_str) # to allow for decimals
        if math.isnan(num): ###REVISED. invalid nan
            return True
    except ValueError:
        return True
    return False # when number is a float function will reach this line and it will return False.


def get_number(prompt_message):
    '''###REVISED. helper function, ask the user for input number'''
    prompt(prompt_message)
    number = input()

    while invalid_number(number):
        prompt('invalid_number')
        number = input()

    return float(number)

def get_operation():
    '''###REVISED. helper function, get operation'''
    prompt('operation_prompt')
    operation_input = int(input())

    # check if the operation value is valid
    while operation_input not in [1, 2, 3, 4]:
        prompt('invalid_operator')
        operation_input = input()

    return operation_input

def perform_operation(num1, num2, operation_f):
    '''###REVISED. Helper function. Perform the operation on the two numbers'''
    try:
        result_operation = None #Initialize variable before match statement

        match operation_f:
            case 1:
                result_operation = num1 + num2
            case 2:
                result_operation = num1 - num2
            case 3:
                result_operation = num1 * num2
            case 4:
                result_operation = num1 / num2
            case _:
                prompt('invalid_operator')
                # default case to handle unexpected operation values

        return result_operation

    except ZeroDivisionError: ###REVISED. check for ZeroDivisionError
        prompt('zero_division_error')
        return None
        # Add a return value for error case to avoid unexpected behavior

prompt('welcome')

while True:

    ###REVISED. Ask the user for the numbers and transform input to floats
    number1 = get_number("first_number")
    number2 = get_number("second_number")

    prompt('chosen_numbers')
    print(f'=> {number1} & {number2}')

    ###REVISED. Helper function, get operation
    operation = get_operation()

    ###REVISED. Helper function. Perform the operation on the two numbers
    output = perform_operation(number1, number2, operation)

    # Print the result to the terminal
    if output is not None:
        prompt('result')
        print(f'=> {output}')

    #Part 3-1. Ask user for another operation (thanks to while True loop)
    prompt("another_operation")
    answer = input()

    if answer and answer[0].lower() not in ('y', 's'):
        break ###REVISED. accepting both languages input
    #We use "and" operator to check an empty case
    #To make sure that if it is an empty string doesn't raise an IndexError
