# 1. Exercise

num = 5

def my_func():
    print(num)

my_func()

It will print 5. We can access the global variable "num" from the local scope of my_func().

# 2. Exercise

num = 5

def my_func():
    num = 10

my_func()
print(num)

It will print 5. The variable num = 5 and num = 10 are different variable,s one is global and one is local.
We cannot reassign the variable num on line 1 within the function (local scope)

# 3. Exercise

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

It will print 10. After using the global keyword, we can access and reassign the global variable within the function (local scope)

# 4.
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

It will print "Hello World". The outer function defines a local variable and the inner function defines another, when outer() is called, inner() is also called within and both functions are printed <print(outer var, inner var)>

# 5.

def my_func():
    num = 10

my_func()
print(num)

It will print NameError, since variable num doesn't exist in the global scope. The local variable is only accessible within the scope.

# 6. Exercise

It will print "Inner 1:25 Inner 2:15", when the first nested function is called, it defines its own local variable X, when the second function is called, it cannot access its peer scope, and it accesses the global variable.