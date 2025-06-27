# ##1 What does this print and why?

# name = 'John' # initializing global variable

# def greet():
#     print(f"Hello, {name}!") #access global var, string interpolation, variable name interpolated into the string

# greet() # call function # hello, John!

# ##2 What does this print and why?

# def assign():
#     var = 20 # local variable var
#     print(var) # access local var defined within the function

# assign() # call function and it will print ->## 20

# ##3. What does this print and why?

# try: # we re using the blocks/statements: try and except
#     print(var) # local, global, variable var hasn't been defined
# except NameError as e: # captures the actual exception object and assigns it to the variable e. This gives you access to the exception details.
#     print("Error occurred") ### Error occurred

# # else: finally: other related blocks

# ### it will print Error occurred and avoid raising the NameError

# ## 4 What does this print and why?

# var = 10 # global variable 'var'

# def function1():
#     var = 20 #initializing local variable 'var'
#     print(var) # print local var

# function1() ### 20

# try:
#     print(var) # access global var ### 10
# except NameError:
#     print("Error occurred")

# def function2(): # defining function 2
#     var += 5 # augmented assignment, try to access variable var, but it will raise and UnboundLocalError, since the variable has not been assigned before using augmented assignment within the function.
#     print(var)

# try:
#     function2()
# except UnboundLocalError:
#     print("Error occurred") ### Error occurred

# def function3():
#     global var #keyword global -> access global var and assign the value 10
#     var += 5 # augmented assignment will work since the variable was assigned before, result 15 (reassignment)
#     print(var)

# function3() ### 15
# print(var) # access global variable var, that was reassigned within function3 ### 15

# # final output:
# 20
# 10
# Error ocurred
# 15

