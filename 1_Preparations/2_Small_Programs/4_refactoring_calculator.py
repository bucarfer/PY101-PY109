'''
Part 2, Refactoring Calculator
Command line calculator program:
-Ask the user for two numbers.
-Ask for the operation: add, subtract, multiply or divide.
-Perform the calculation and display the result'''

#Part 3-2. Importing messages to the file from a JSON configuration file
import json

#Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

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
        float(number_str) # to allow for decimals
    except ValueError:
        return True
    return False

prompt('welcome')

while True:
    # Ask the user for the first number
    prompt("first_number")
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    # Ask the user for the second number
    prompt("second_number")
    number2 = input()

    # check if number2 is valid
    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('chosen_numbers')
    print(f'=> {number1} & {number2}')
    # Ask the user for an operation to perform

    prompt("operation_prompt")
    operation = input()

    # check if operator value is valid
    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operator')
        operation = input()

    # Perform the operation on the two numbers
    number1 = float(number1)
    number2 = float(number2)
    match operation:
        case '1':
            output = number1 + number2
        case '2':
            output = number1 - number2
        case '3':
            output = number1 * number2
        case '4':
            output = number1 / number2

    # Print the result to the terminal
    prompt('result')
    print(f'=> {output}')

    #Part 3-1. Ask user for another operation (thanks to while True loop)
    prompt("another_operation")
    answer = input()

    if answer and answer[0].lower() != 'y':
        break
    #We use "and" operator to check an empty case and make sure that if it is an empty string doesn't raise an IndexError
