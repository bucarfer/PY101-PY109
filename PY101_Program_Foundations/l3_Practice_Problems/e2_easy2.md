## Question 1. Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]

# Opt 1
reverse_numbers = numbers.reverse()
print(reverse_numbers)
### This option was wrong because it mutates the list

# Opt 2
reverse_numbers = numbers[::-1]
print(reverse_numbers)

# Opt 3, LS solution
reversed_numbers = list(reversed(numbers))

## Question 2. Given a number and a list, determine whether the number is included in the list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8
number2 = 95

number1 in numbers #False
number2 in numbers #True

## Question 3. Programmatically determine whether 42 lies between 10 and 100, inclusive. DO the same for the values 100 and 101.

number1 = 42
10 <= number1 <= 100 #True

100 in range(10,101) #True
101 in range(10,101) #False (includes start but not end value)

## Question 4. Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number at index 2.

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers) # [1, 2, 4, 5]

# Option LS
del numbers[2]
print(numbers) # [1, 2, 4, 5]

## Question 5. How would you verify whether the data structures assigned to the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

isinstance(numbers, list) #True
isinstance(table, list) #False

# this also works but has potential issues
type(numbers) is list #True
type(table) is list #False

## Question 6. If we have a 40-character wide table of Flintstone family members, how can we center the following title above the table with spaces?

title = "Flintstone Family Members"
centered_title = title.center(40)

## Question 7. write a one-liner to count the number of lowercase t characters in each of the following strings:

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

statement1.count("t") #2
statement2.count("t") #0

## Question 8. Determine whether the following dictionary of people and their age contains an entry for 'Spot'

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
'Spot' in ages #False

## Question 9. We have most of our Munster family in our ages dictionary:
# Add the entries for Marily and Spot to the dictionary

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

ages['Marilyn'] = 22
ages['Spot'] = 237
print(ages)

# LS solution:
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)