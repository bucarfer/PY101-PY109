##list methods: len(list), list.append(), list.pop(), list.reverse()
# What does this print and why the following examples?

##1
my_list = [1, 2, 3, 4, 5] # global variable init
length_of_list = len(my_list) # global variable init - 5
print("Length of the list:", length_of_list, sep=',') #
# Length of the list:5
#when we print items with commas it adds automatically spaces

##2
lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_two)
else:
    print(lst_one)

print(lst_one)
# we are assigning lst_two and mutating lst_one

##3
my_list = [1, 2, 3, 4, 5] # global variable - my list
ele = my_list.pop() # global variable - ele = 5
print("Popped element:", ele) # "Popped element: 5"
print("List after popping:", my_list) # List after popping: [1, 2, 3, 4]
ele1 = my_list.pop(1) # global variable - ele1 - my_list = [1, 3, 4] - 2
print("Popped element at index 1:", ele1) # Popped element at index 1: 2
print("Modified list after popping at index 1:", my_list)
# Modified list after popping at index 1: [1, 3, 4]

##4
elements = [0, 1 , 2, "Dima"]
print(elements.reverse()) # .reverse() returns None
print(elements) # prints mutated list

##5
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
} # assign a new global variable

def get_val_of_dimo(info):
    try:
        info['dimo'] # output = 31 (no return, function will print None)
        return  info['dimo'] #31 # return value 31, no need for variable
    except KeyError: # avoid raising an error
        return "Typo"

print(get_val_of_dimo(ages)) #31

##6
my_dict = {'a': 1, 'b': 2, 'c': 3} # initialization of my_dict with dictionary object
keys = my_dict.keys() # initialization of keys with my_dict.keys(), where the method keys will create a new collection of the keys from my_dict
print(keys) # it will print the collection of keys
for key in keys: # for loop that iterates through the iterable keys
    print(key) # for each key in keys, the code will print the key
    # dict_keys(['a', 'b', 'c']) dynamic view object
    # a
    # b
    # c # no quotes for printing keys
my_dict['d'] = 4 # new pair
print(keys) # new dynamic view object 'keys' -> dict_keys(['a', 'b', 'c', 'd'])

##7
my_dict = {'a': 1, 'b': 2, 'c': 3} # assign global my_dict
values = my_dict.values() # global variable values -> dynamic view object([1, 2, 3])
print(values) # dict_values([1, 2, 3])
for value in values: # for loop iterates each value of the collection within the dynamic view object
    print(value)

# dict_values([1, 2, 3])
# 1
# 2
# 3

##8
my_dict = {'a': 1, 'b': 2, 'c': 3} # init global variable, my_dict,
items = my_dict.items() # assigning the new variable "items" -> dynamic view object
print(items) # my_dict_items[('a': 1, 'b': 2, 'c': 3)]
for key, value in items: #iterating all pairs within the items collection
    print(key, value) #print each pair of the dictionary in a new line

# output
# dict_items([('a': 1), ('b': 2), ('c': 3)]) # this is how .items returns values
# a 1 # prints pair key-value without brackets and separate by an space
# b 2 # prints pair key-value without brackets and separate by an space
# c 3 # prints pair key-value without brackets and separate by an space
