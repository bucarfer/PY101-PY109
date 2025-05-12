## Question 1. Will the code below raise an error?
numbers = [1, 2, 3]
numbers[6] = 5

Yes, it will raise an IndexError because the index is out of range.

## Question 2. How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def string_ends(str):
    return str.endswith("!")

print(string_ends(str1))
print(string_ends(str2))

## Question 3. Starting with the string: famous_words = "seven years ago..."

# Option 1, string concatenation
famous_words = "seven years ago..."
four_score = "Four score and "
combined_string = four_score + famous_words
print(combined_string)

# Option 2, convert into list and append new list
famous_words = "seven years ago..."
four_score = "Four score and "
combined_list = list(four_score) + list(famous_words)
"".join(combined_list)

# Option 3 (LS), string interpolation
new_string = f"Four score and {famous_words}"

## Question 4. Using the following string, print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.capitalize())
"""It transforms the string with first letter capitalize and the rest in lowercase"""

## Question 5. Switch the case of the following string:
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

## Question 6. Determine whether the name Dino appears in the string below -- check each string separately

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# Option 1
str1.find("Dino") #-1 [it doesn't appear]
str2.find("Dino") #41 [index where appear]

# Option 2
"Dino" in str1 #False
"Dino" in str2 #True

## Question 7. How can we add the family pet "Dino" to the following list?

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")

## Question 8. How can we add multiple items to our list. Replace the call to append for another method invocation.

flintstones.extend(["Dino", "Hoppy"])

## Question 9. Print a version of the following sentence removing everything after the word house:

advice = "Few things in life are as important as house training your pet dinosaur."

# My solution:
advice.find("house")
new_advice = advice[0:38]
print(new_advice)

# LS solution:
print(advice.split("house")[0])
# In this solution we split the string into two, using as a separator the word house, and after we print the first index of the list.

## Question 10. Print the following string with the word important replaced by urgent.

advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important", "urgent"))
