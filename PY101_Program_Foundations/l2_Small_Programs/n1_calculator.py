'''Our first program in this course will be a command line calculator program that will:

Ask the user for two numbers.
Ask the user for the type of operation to perform: add, subtract, multiply or divide.
Perform the calculation and display the result'''

print('Welcome to calculator!')
# Ask the user for the first number
print("What's the first number?")
number1 = input()
# Ask the user for the second number
print("What is the second number?")
number2 = input()

print(f'the chosen numbers are: {number1} and {number2}')
# Ask the user for an operation to perform
while True:
    print("What operation would you like to perform? \n1) Add 2) Subtract 3)Multiply 4)Divide")
    operation = input()
    if operation in ['1', '2', '3', '4']:
        break
    else:
        print('Invalid input. Please choose 1, 2, 3, or 4')
# Perform the operation on the two numbers
if operation == '1': # '1' represents addition
    output = int(number1) + int(number2)
elif operation == '2': # '2' represents subtraction
    output = int(number1) - int(number2)
elif operation == '3': # '3'represents multiplication
    output = int(number1) * int(number2)
elif operation == '4': # '4' represents division
    output = int(number1) / int(number2)
else:
    print('write a number from 1 to 4 to perform an operation')
# Print the result to the terminal
print(f'The result is: {output}')