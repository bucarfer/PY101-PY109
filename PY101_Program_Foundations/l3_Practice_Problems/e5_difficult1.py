### Will the following functions return the same results?

def first ():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first()) # {'prop': "hi there"}
print(second()) # None, but doesn't raise any error as I thought

## These functions do not return the same thing as shown above in the output comments, if there is nothing after return function, Python will print None, all lines below will be ignored

### Question 2. What does the last line in the following code output?

dictionary = {'first':[1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list) #[1, 2]
print(dictionary)  #{'first':[1, 2]}

## Solution, since num_list is reference to the original dictionary, appending the number it will affect the original dictionary and the list.

# Option 1. If instead of affecting the original dictionary, we want to modify my_list but not dictionary, we have to create a copy

dictionary = {'first':[1]}
num_list = dictionary['first'].copy()
num_list.append(2)

# Option 2. We can also use slicing, since it will create a copy.

dictionary = {'first':[1]}
num_list = dictionary['first'][:]
num_list.append(2)

# reminder of slicing
# nums = [0, 1, 2, 3, 4, 5]
# nums[1:4]     # ➜ [1, 2, 3]
# nums[:3]      # ➜ [0, 1, 2]     (from start)
# nums[3:]      # ➜ [3, 4, 5]     (to end)
# nums[::-1]    # ➜ [5, 4, 3, 2, 1, 0]  (reversed)
# nums[:]       # ➜ [0, 1, 2, 3, 4, 5] (full shallow copy)

### Question 3. Given the following similar sets of code, what will each code snipped print?

#A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Solution A -> In the three examples the variables inside the functions (locals) are different from the variables outside (global)
# Since the variables are local, reassigning them does not affect the original list.
# In option A there is a reassignment only. We are not modifying the list contents, only swap the labels between them.

# one is: ['one']
# two is: ['two']
# three is: ['three']

#B
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Solution B -> Same as example A. Functions reassigned do not affect original list.
# In option B, there is a new list assignment, brand new lists as parameters of the function.

#C
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Solution C ->  In this case mess_with_vars modifies the content of the list directly, since lists are mutable, we are changing the actual objects and the changes will be reflected outside the function.


# one is: ['two']
# two is: ['three']
# three is: ['one']

### Question 4. Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

# Alyssa's function to determine if a string is between 0 and 255

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

# Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid." Help Ben fix his code.

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    # create a list with variables between dots
    if len(dot_separated_words) != 4:
        return False

    for word in dot_separated_words: # loops through all list items
        if not is_an_ip_number(word):
            # returns False if is not a string between 0 and 255
            return False

    return True

print(is_dot_separated_ip_address("10.4.5.11") )   # True
print(is_dot_separated_ip_address("10.4.5.300"))   # False (300 is too big)
print(is_dot_separated_ip_address("10.4.5")    )   # False (only 3 parts)
print(is_dot_separated_ip_address("10.4.5.abc"))   # False (non-numeric)

### Question 5. What do you expect to happen when the greeting variable is referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

## Solution. NameError, variable not defined
# the greeting variable is not uninitialized, block not executed due to False condition

## Remember, in Python variables assigned inside an if, for, or while block (without being inside of a function) are still global and can be accessed.

# Example:

if True:
    greeting = "hello world"

print(greeting)  # Prints: hello world
