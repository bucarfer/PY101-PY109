## Question 1. Write two different ways to remove all the elements from the following list:

numbers = [1, 2, 3, 4]

# option 1
numbers.clear()
print(numbers)

# option 2
while numbers:
    numbers.pop()
print(numbers)

# option 3, extra option that also works (but slower)
while numbers:
    del numbers[0]
print(numbers)

## Question 2. What will the following code output?

print([1, 2, 3] + [4, 5])
# output [1, 2, 3, 4, 5]

## Question 3. What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
# output "hello there"

str1 = "hello there"
str2 = str1
str1 = "goodbye!"
print(str2)
# output "hello there"

# "hello there", in Python the assignment of one variable to another variable makes both variables to point to the same object, but once we assign a new object to one of the variables the connection breaks.

## Question 4. What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
# output [{'first': 42}, {'second': 'value2'}, 3, 4, 5]

# Since it is a shallow copy both my_list1 and my_list2 are pointing to the same dictionary in memory, when we replace the value of the first dictionary, the change shows up in both lists.
# If we want fully independent list where we duplicate all objects, not only the outermost layer, we have to use the deepcopy() function.

## Question 5. The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this functions so it only has one return statement and does not explicit use either True or False?

def is_color_valid(color):
    color == "blue" or color == "green":
        return True
    else:
        return False

# Option 1. IN functions that return a boolean you don't need to specify True or False, a more Pythonic way is to return the value of a conditional expression directly.

def is_color_valid(color):
    return color == "blue" or color == "green"

# Option 2. We can also use the in operator to check if the color exists in a list with all the options.

def is_color_valid(color):
    return color in ["blue", "green"]