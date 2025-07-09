## 1. What do these print and why? Truthiness in Python
truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print("Values:")
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

# Explanation: In Python, 0, '', [], {}, None, and False are considered falsy. Everything else is truthy.

##2. What do these print and why?

x = 5
y = 10
z = 15

print(x > 0 and y < 20)     # True
print(not x == y)           # True
print(x < y and y < z)      # True
print(x > y or y > z)       # False
print(not (x > y))          # True

##3. find below n3 and continue from here ---------------------


# 1. Boolean logic example

num = 12

if num / 3 < 3 and num > 10:  # False and True => False
    print("Hello")
elif num >= 8 and num < 6 or num > 4 and num < 16:  # (num >= 8 and num < 6) or (num > 4 and num < 16): True and True => True
    print("Hello 2")  # Output
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")

# Explanation: Only the second condition is True, so it prints "Hello 2"



# 3. Errors with division
# Uncomment to see error:
# if [1/0]:  # ZeroDivisionError
#     print("no error!")

if [None]:
    print("[None] is truthy")

# Explanation: [None] is a list with one item, so it's truthy.

# 4. Chained comparison

a = 10
b = 20
print(a < b < 30)  # True
print(a > b or b == 20)  # False or True -> True

# 5. Membership testing
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 not in my_list)  # True

# 6. Reversing list

elements = [0, 1, 2, "Dima"]
print(elements.reverse())  # None
print(elements)  # ['Dima', 2, 1, 0]

# Explanation: reverse() mutates list in-place and returns None

# 7. Nested function and scope example

def function1():
    x = 10

    def function2():
        y = 20
        print(x)  # 10

    function2()
    print(x)  # 10

function1()
# print(x)  # NameError
# print(y)  # NameError

# 8. Shadowing outer variable

def function1():
    x = 10

    def function2():
        x = 20
        print(x)  # 20

    function2()
    print(x)  # 10

function1()
# print(x)  # NameError
# print(y)  # NameError

# 9. Attempt to use 'nonlocal' incorrectly
# Uncommenting this will raise a SyntaxError
# def function1():
#     x = 10
#     def function2():
#         nonlocal x
#         x = 20
#         print(x)
#     function2()
#     print(x)
# function1()

# 10. Using global to mutate outer variable

def function1():
    x = 10

    def function2():
        global x
        x = 20
        print(x)  # 20

    function2()
    print(x)  # still 10, because local x is not affected by global x

function1()
# print(x)  # Now x exists globally

# 11. Global/local distinction

var = 10

def function1():
    print(var)  # 10

function1()

def function2():
    var = 20
    print(var)  # 20

function2()
print(var)  # 10

# 12. Dictionary KeyError handling
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dimo(info):
    try:
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dimo(ages))  # 31

# Explanation: 'dimo' exists as key so value is returned. Error would be caught otherwise.


num = 12

if num / 3 < 3 and num > 10: # if ((num / 3) < 3) and (num > 10): # False
    print("Hello")
elif num >= 8 and ((num < 6 or num > 4) and num < 16): # True and (True and True) # True
    print("Hello 2") # Hello 2
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")

'''
(num >= 8 and num < 6) or (num > 4 and num < 16) # False or True -> True
'''




