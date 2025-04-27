'''
Part 2, Refactoring Calculator
Our first program in this course will be a command line calculator program that will:

Ask the user for two numbers.
Ask the user for the type of operation to perform: add, subtract, multiply or divide.
Perform the calculation and display the result'''

# new print function to add message before each line
def prompt(message):
    """display message to user with prefix"""
    print(f'==> {message}')

prompt('Welcome to calculator!')
# Ask the user for the first number
prompt("What's the first number?")
number1 = input()

# check if number1 is valid
def invalid_number(number_str):
    """returns True if input cannot be converted to a float"""
    try:
        float(number_str) # to allow for decimals
    except ValueError:
        return True

    return False

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number")
    number1 = input()


# Ask the user for the second number
prompt("What is the second number?")
number2 = input()

# check if number2 is valid

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number")
    number2 = input()

prompt(f'the chosen numbers are: {number1} and {number2}')
# Ask the user for an operation to perform

prompt("What operation would you like to perform? \n1) Add 2) Subtract 3)Multiply 4)Divide")
operation = input()

# check if operator value is valid
while operation not in ['1', '2', '3', '4']:
    prompt('Invalid input. You must choose 1, 2, 3, or 4')
    operation = input()

# Perform the operation on the two numbers
match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

# Print the result to the terminal
prompt(f'The result is: {output}')
