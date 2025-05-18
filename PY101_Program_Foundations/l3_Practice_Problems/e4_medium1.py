### Question 1. write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:

# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!

# My solution
def the_flintstones_rock():
    flint = "The Flintstones Rock!"
    counter = 1
    while counter <= 10:
        flint = "-" + flint
        print(flint)
        counter += 1

the_flintstones_rock()

# LS solution

for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')

### Question 2. Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

## Bonus Question: What is the purpose of number % divisor == 0 in that code?
# it checks if the divisor divides the number evenly (with no reminder), what is the definition of a factor

# The % operator (modulo) returns the remainder
# the // operator (floor division) is a integer division, returns the whole number part, without the decimals

### Question 3. Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer, What is the key difference between these implementations?

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Solution, in the first function we are mutating the buffer list, in the second function we are not mutating, instead we are creating a new list that gets assign to the buffer

### Question 4. What will the following two lines of code output?

print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)

# Solution, the outputs are: 0.9 and True (I was wrong)

# LS solution, If you thought that the outputs would be 0.9 and True, respectively, you were wrong.
0.8999999999999999
False
we need to use math.isclose function as a way around for this problem

import math
print(0.3 + 0.6) # 0.9
print(math.isclose(0.3 + 0.6, 0.9)) # True

### Question 5. What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# The output is False because nan (not a number) is a special number value and Python doesn't let you use ==

## Bonus question. How can you reliably test if a value is nan?
# Solution, to test if a value is nan, you can use the math.isnan() function:

import math
nan_value = float("nan")

### Question 6. What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# solution. result is 34

### Question 7. One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        #key,value loops over each item,dict.items gets all key_value pairs
        value["age"] += 42
        value["gender"] = "other"

## What does the following code output?

mess_with_demographics(munsters)

## Solution, It mutates the whole dictionary. it is a nested dictionary, the individual family member's data are the ones being mutated in this example. If we didn't want to affect the original copy we could create a deep copy:

import copy

def safe_mess_with_demographics(demo_dict):
    new_dict = copy.deepcopy(demo_dict)  # full dict clone

    for key,value in new_dict.items():
        # we use "for key/value" to loop over each person
        value['age'] += 42
        value['gender'] = 'other'

    return new_dict

new_munsters = safe_mess_with_demographics(munsters)
print(munsters)
print(new_munsters)

## If we wanted to mutate only one individual family member:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_member_demographics(demo_dict, family_member):
    if family_member in demo_dict: # we use "if" to modify specific person
        demo_dict[family_member]["age"] += 42
        demo_dict[family_member]["gender"] = "other"

    print(f'{family_member} is {demo_dict[family_member]}')

mess_with_member_demographics(munsters, "Herman")

### Question 8. Function and method calls can take expressions as arguments. Suppose we define a function named rps as follows, which follows the classic rules of the rock-paper-scissors game, but with a slight twist: in the event of a tie, it just returns the choice made by both players.

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

## What does the following code output?

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

## solution, "paper". Nested function with ternary conditionals.

1. rock vs paper -> paper
2. rock vs scissors -> rock
3. paper vs rock -> paper
4. paper vs rock -> paper

## Question 9. Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo()) or "no"

# What will the following function invocation return?

bar(foo())

1. bar("yes")
2. False and ... -> False ## Python shortcircuit and gives the answer of False, with the operator "and" if the first value is False, python doesn't have to continue, it knows it will be always False, independently of of the second value, it is why it doesn't have to check it

### Question 10. In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning". Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id (c))

## Solution. True, the id of a and c is the same, b has the same id as a and c due to interning, therefore the output is True.
