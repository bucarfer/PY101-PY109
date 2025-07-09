## 1: What coercion is happening here? Is it implicit or explicit?

x = 3.5
y = 5
z = x + y

# It is an implicit coercion, when we combine floats and integers the result is a float.
# (The variable x is assigned to the float 3.5, the variable y is assigned to the integer 5.
# The variable z is assigned to the evaluated result of x + y. When x and y are added, y is implicitly coerced to a float as Python can not add different variable types. This is an example of implicit coercion.

## 2: What coercion is happening here? Is it implicit or explicit?

a = 1
b = 2
print(a + b)  #solution:  3, implicit coercion, int -> str with the use of print instead of a constructor
# The print function coerces the 3 into a string, the print() function always coerces any argument into strings. This is an example of implicit coercion)

## 3: What coercion is happening here? Is it implicit or explicit?

month = "December"
day = int(input("What day is it? "))
print(f"Today is the {day} of {month}")

# solution:
month = "December"
day = int(input("What day is it? ")) # explicit coercion, str -> int , constructor int()
print(f"Today is the {day} of {month}") # implicit coercion, int -> str with string interpolation

