### Basic questions:

# Is a range primitive or non-primitive? Non primitive
# Is a range mutable or immutable? Immutable
# Does range have a literal form or a type constructor? type constructor range
# Is a range a sequence or a collection? it is a sequence of ordered integers
# What is the most common use of the range datatype? For loops for iterations
# Are ranges homogenous or heterogeneous? homogeneous (int, same type)
# Why are ranges considered lazy. Because they dont show the whole list of elements which include the range, only the beginning, end and steps (this saves memory) Only shows all the elements when we iterate or convert the range into a list.

**## 1. What do these print and why? What concept does this demonstrate?

print(range(0,10))
print(len(range(5, 15)))
print(my_range[1])
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))

# range(0,10)
# 10
# NameError, my_range is not defined
# name(3, 7)
# [12, 11, 10, 9]
# [] ** surprise!!
# False
# false

## It demostrates that range are a immutable lazy sequence of integers defined by a start, stop minus 1, and an optional step. It behaves like a list in iteration, indexing, and membership test(in, not in), but without generating the values upfront.

## 2. What do these print and why? What concept does this demonstrate?

example = range(0)
if example:
    print(list(example))
else:
    print(example)

# range(0) creates an empty range, what evaluates as Falsy and runs the else block printing -> range(0,0)
# Demonstrates the concepts of falsy and truthy and that even non empty objects like range(0) can behave like an empty one in conditionals.

## 3. What do these print and why? What concept does this demonstrate?

def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if 50 < n <= 100:
            print(f'{number} is between 51 and 100')
        case _:
            print(f'{number} is greater than 100')
number_range(0)
number_range(25)

# 0 is between 0 and 50
# 25 is between 0 and 50
# Explanation: In this example, we’re checking which range the number falls into using match and conditional guards. The number 0 satisfies the second condition (n <= 50), so it prints "0 is between 0 and 50". The number 25 also satisfies the same condition, so it prints "25 is between 0 and 50".
# This demonstrates the use of pattern matching with guards (case n if ...) to control flow based on conditions.
