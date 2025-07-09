##1 What does this print and why?

name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()

# hello, John!
# Explanation: n this example, we initialize the variable name, assigning it the string 'John'. Then we define a function greet() that uses string interpolation (f-string) to print "Hello, {name}!". When we call greet(), Python looks for the value of name. Since there is no local variable named name inside the function, it accesses the global variable defined outside of it. As a result, the output is "Hello, John!". This demonstrates Python's use of variable scope resolution, where it checks the local scope first, and if not found, it searches the enclosing/global scope.

##2 What does this print and why?

def assign():
    var = 20
    print(var)

assign()

# call function and it will print ->## 20
# In this second example, we define a function called assign that, within its body, creates a local variable named var, assigning it the integer value 20. The function then prints the value of var. When we call assign() on the line below, Python executes the function, creating var within the local scope of the function and printing its value. Therefore, the output will be 20. After the function finishes running, the variable var no longer exists outside of the function’s scope.

##3. What does this print and why?

try: # we re using the blocks/statements: try and except
    print(var)
except NameError as e:
    print("Error occurred")

# local, global, variable var hasn't been defined
# captures the actual exception object and assigns it to the variable e. This gives you access to the exception details.
# prints output #"Error occurred"
#Explanation: In this third example, we use the try and except blocks. First, we attempt to print the value that the variable var is pointing to. Then, we have an except block that will be executed if the try block raises a NameError. Since in this piece of code we haven't defined the variable var before calling it, the try block will raise a NameError, and the except block will run, printing "Error occurred"

## 4 What does this print and why?

var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)

# final output:
# 20
# 10
# Error occurred
# 15
# Explanation: In this fourth example, we start by initializing the global variable var with the value 10. Then, we define function1, which creates a local variable also named var and sets it to 20. When function1 is called, it prints the local value 20. After that, we run a try block where we print var. Since the global var still exists and hasn't been affected by function1, Python accesses it and prints 10. Next, we define function2, which attempts to increment var using augmented assignment (var += 5). However, since Python treats var as a local variable and it hasn't been assigned yet within the function, this raises an UnboundLocalError, and the except block prints "Error occurred". Lastly, we define function3, where we explicitly declare var as a global variable using the global keyword. This allows the function to both access and modify the global variable. Inside function3, var is incremented by 5, changing its value to 15, which is then printed. When we print var again outside the function, it also shows 15, confirming that the global variable was successfully modified from within the function.

## 5. What does this print and why?

var = 10

def function1():
    print(var)

function1()

def function2():
    var = 20
    print(var)

function2()
print(var)

# 10
# 20
# 10
# Explanation: In the following example, we initialize the variable var pointing to the integer 10. Then we define the function 1 where we print var. In this case, function 1 accesses the global variable var and its value 10. And when we call function 1 in line 74, we print the value of 10. In the second example, we initialize the variable var inside the function 2, which is a local variable, and when we print var, the function 2 accesses the variable var in the local scope, and prints the value 20 when we call function 2. Finally, when we print var outside the function scope, we print the global variable var, still pointing to the value 10. Since the local variable var was initialized inside the function and didn't affect the global variable. Concept of Global scope vs local scope.

## 6. What does this print and why?

def function1():
    x = 10

    def function2():
        y = 20
        print(x)

    function2()
    print(x)

function1()
print(x)
print(y)

# 10
# 10
# NameError, name x is not defined (doesn't exist int the global scope)
# Python raises the error above and stops execution before arriving to this line, if the line print(x) didn't exist, this last line will also print NameError.

## explanation: In this example, we define a function `function1` where a local variable `x` is assigned the value 10. Inside `function1`, we define another nested function called `function2`, which creates its own local variable `y = 20` and then prints the value of `x`. Because `function2` is defined inside `function1`, it has access to `x` through lexical scoping, so it prints `10`. After calling `function2`, `function1` also prints `x`, which again outputs `10`. However, once `function1` finishes executing, both `x` and `y` are no longer accessible, as they were defined in local scopes. Therefore, the final two lines, `print(x)` and `print(y)`, raise `NameError` exceptions because those variables are not defined in the global scope. This demonstrates how **nested functions** can access variables from their enclosing scope, but such variables do not persist outside their local context.

## 6. What does this print and why?

var = 10

def access():
    print(var)

## Output: Nothing

# Why: In this example, the variable var is assigned the value 10, and a function called access is defined, which prints the value of var. However, since the function is only defined but never called, the code produces no output. Python registers the function, but does not execute its body unless explicitly invoked.

# Do again problems 1 to 4