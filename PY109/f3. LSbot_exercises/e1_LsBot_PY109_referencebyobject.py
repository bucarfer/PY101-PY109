## Example 1: Understanding parameters and arguments
def multiply(x, y):  # x and y are parameters
    return x * y

a = 5
b = 6
result = multiply(a, b)  # a and b are arguments (variables)
print(result)  # What will this print?

# Solution 1: the function will print 30, that are the specific values passed to the function when it is called.

## Example 2: Understanding pass by object reference with immutable objects
def modify_string(text):
    text = text + " modified"  # Reassignment
    print(f"Inside function: {text}")

message = "Hello"
modify_string(message)
print(f"Outside function: {message}")  # What will this print?

# Solution 2
# Inside function: Hello modified -> prints the reassign local variable
# Outside function: Hello -> prints the global variable that hasn't been modified

# This example demonstrates that strings are immutable and how Python uses "pass by object reference". In line 14 we are creating a new string and making text point at it, this reassignment only affects the local variable.

## Example 3: Understanding pass by object reference with mutable objects
def modify_list(items):
    items.append("new item")  # Mutation
    print(f"Inside function: {items}")

my_list = ["item1", "item2"]
modify_list(my_list)
print(f"Outside function: {my_list}")  # What will this print?

# Solution 3.
# Inside function: ["item1", "item2", "new item"] -> We print the new "My_list" version after being mutated
# Outside function: ["item1", "item2", "new item"] -> Prints the same output since we have mutated the original variable
# This demostrates a crucial concept of pass by object behaviour on mutable objects, when a mutable object like a list is passed to a function, both the local variable and the original (global) see the changes because they reference the same object.