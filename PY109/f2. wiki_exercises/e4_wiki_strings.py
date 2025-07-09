### Basic questions
# Are strings mutable or immutable? (Immutable)
# Are strings primitive or non-primitive? (Primitive)
# Are strings literals? (Yes)
# What is a text sequence? (strings of characters)
# What kind of characters are used in a string? (Unicode characters)
# Are text sequences the same as ordinary sequences? (No, text sequence contain only string characters. ordinary sequences refer to any other sequence types that store multiple elements (e.g. lists, tuples, ranges))

## 1. What is the output of this code, and why? What is the concept covered here?

str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1) #orld
sub2 = str1[::-1]
print(sub2) # !dlrow ,olleH
sub3 = str1[::2]
print(sub3) #Hlo ol!

# The concept is string slicing, which creates a new string object, a substring for each case.

## 2. What is the output of this code, and why? What is the concept covered here?
print("Hello\nWorld")
#Hello
#World

# This demonstrates the escape character. It will create a new line after the string Hello with the string World.

## 3. What is the output of this code, and why? What is the concept covered here?

name = 'Alexander Graham Bell'
print(name[0])

#A it will print the first character of the string that the variable name is pointing it demonstrates that strings can be accessed with indexing syntax.

### f-strings

## 1. . What does this print and why, what is the concept?

name = 'Abraham Lincoln'
print(f"{name} was a President of the US")

# (This will print Abraham Lincoln was a President of the US. The f prefix in the print function allows the value of the variable to be interpolated and merged with the rest of the print statement. This demonstrates f-strings.)

### String Methods

## 1. What does this print and why?

mashup = "thIs is How we type careLEssly"
cleaned = mashup.capitalize()
print(cleaned) # This is how we type carelessly ##capitalize only first word
# title for all words

## 2. What do these print and why?

stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)  # 'tHIS iS bACKWARDS'
print(str1)  # 'This Is Backwards'
print(str2)  # 'THIS IS BACKWARDS'
print(str3)  # 'this is backwards'

## 3. What do these print and why?

s1 = "Hello"
print(s1.isalpha()) #True
s2 = "Hello World"
print(s2.isalpha()) #False, there is a whitespace
s3 = "Hello!"
print(s3.isalpha()) #False
s4 = "Hello123"
print(s4.isalpha()) #False
s5 = ""
print(s5.isalpha()) ##False, no characters -> empty
s6 = "こんにちは"
print(s6.isalpha()) ##True  (includes all alphabetic characters from all languages within the unicode standards)
s7 = "HelloWorld"
print(s7.isalpha()) #True
words = ["apple", "banana", "cherry"]
print(all(word.isalpha() for word in words)) # True

##explanation of last one
#generator expression, doesn't print anything
# generator expression iterates through each word in words and calls the method .isalpha() (which returns True or False)
# If you want to see the individual boolean values, you need to convert it to a list:
# words = ["apple", "banana", "cherry"]
# print(list(word.isalpha() for word in words))  # [True, True, True]

# The all() function takes an iterable and returns:
# -True - if no falsy elements
# -False, if any element is Falsy

# print(all([]))        # True - if no falsy elements (empty list True, because no falsy elements)
# print(any([]))        # False - if no truthy elements (empty list False, because no Truthy elements)

# dont confuse this with a ternary expression, also called a conditional expression, the ternary expression has this structure:
value1 if condition else value2

## 4. What does this print and why?
string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()  # True
result2 = string2.isalpha()  # False
result3 = string3.isalpha()  # False

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)

# Is 'HelloWorld' alphabetic? True
# Is '12345' alphabetic? False
# Is 'Hello World' alphabetic? False

# The .format() method works by replacing {} placeholders in a string with the arguments passed to the method, it creates a new string:
message_format = "Hello, {}. You are a {}."
formatted_message = message_format.format("Victor", "programmer") # -> print(formatted_message) # Output: Hello, Victor. You are a programmer.

# Different Ways to Use .format()

# Positional Arguments (Sequential arguments placed as placeholders in order)
# Indexed Placeholders (Using index instead of sequence/position)
template = "I have {0} apples and {1} oranges. {0} apples are red."
result = template.format(5, 3) -> print(result)
# Output: I have 5 apples and 3 oranges. 5 apples are red.


## 5. What do these print and why?
s1 = "123abc"
print(s1.isdigit()) # False
s2 = "123$%^"
print(s2.isdigit()) # False
s3 = ""
print(s3.isdigit()) # False
s4 = "12345"
print(s4.isdigit()) # True

## 6. What do these print and why?
print("Hello World".isalnum()) #False
print("Hello@World".isalnum()) #False at symbol
print("".isalnum()) #False, empty string
print("Hello.123".isalnum()) #False, dot is not included
print("HelloこんにちはWorld".isalnum()) #True (includes alphabet in all languages)

# .isalnum() returns the boolean True if all the elements are alphabetic(all languages) or digits, therefore alphanumerics.
# Do not confuse with numeric characters than include decimals, negative and positive symbols.

## 7. What do these print and why?

name = 'HELLO'

if name.isupper():
    print("WORLD")
else:
    print("world")

# The str.isupper() method returns True because all cased characters in the string are uppercase and there is at least one cased character. In this case, "HELLO" meets that condition, so name.isupper() is True, and the if block runs, printing "WORLD".

##  8. What do these print and why?

def punctuation_type(str):
    if str == str.upper():
        print('This is all caps')
    elif str == str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3) #

# Solution:
#the three strings are passed into the function one by one when we call the function with each variable (pass by object), the strings pass through the comparison operations, the first one is all capital letters so it will run the if statement 'This is all caps', the second one is all lower cases so it will run the elif statement and print 'This is all lowercases', and finally the third one is a mix of both and it will run the else block printing 'Neither'
# This is all caps
# This is all lowercase
# Neither

##  9. What do these print and why?

str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!   How are you?   "
word_count = sum(1 for word in sentence.split() if not word.isspace())
print("Number of words in the sentence:", word_count)

# Solution:
# True
# False
# False
# Number of words in the sentence: 5
# Explanation: In this exercise, we examine how the .isspace() method works and how to count words in a sentence using .split(). The variables str1, str2, and str3 are assigned different strings. When we apply .isspace(), it returns True only if the entire string consists of whitespace characters and is not empty. Therefore, str1.isspace() returns True because it contains only spaces. str2.isspace() and str3.isspace() return False because they contain letters. In the second part, the variable sentence holds a string with words separated by irregular spacing. Using .split() without an argument splits the string at any group of whitespace characters, effectively separating the sentence into individual words. The generator expression counts each word by checking that it is not made entirely of spaces with not word.isspace(), even though in this case it’s redundant since .split() ensures that. This results in a total word count of 5. This exercise demonstrates how .isspace() checks for space-only strings and how .split() can be used effectively for word counting in strings.


##  10. What do these print and why?

s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))

# Solution:
# "Hello, World"
# "hello, World"
# Explanation: In this exercise, the variable s is assigned a string that includes leading and trailing spaces, along with the content "Hello, World!". The first print(s.strip()) uses the .strip() method without any arguments, which removes all leading and trailing whitespace characters by default. As a result, it returns the string "Hello, World!" with no surrounding spaces. In the second call, s.strip(" !"), the method is passed the characters " !" as an argument. This means that any combination of spaces and exclamation marks will be stripped from both the beginning and end of the string. In this case, the leading spaces and the trailing space and exclamation mark are removed, but characters like commas and internal spaces remain. Therefore, the result is "Hello, World" with the leading and trailing specified characters removed. This exercise demonstrates how .strip() works differently when called with no arguments versus when passed specific characters to strip.

## 11. What do these print and why?

s = "www.example.com"
print(s.lstrip('wcmo.'))

# example.com
# In this exercise, the variable s is assigned the string "www.example.com". We then use the method s.lstrip('wcmo.'). The .lstrip() method removes characters from the left side of the string, stopping as soon as it encounters a character not included in the provided set. In this case, the set 'wcmo.' includes the characters 'w', 'c', 'm', 'o', and '.'. Starting from the left, the method will strip all 'w' characters, followed by the '.', and then the 'c' and 'o' from "com" if found consecutively. However, it does not treat the input as a prefix but rather as a set of characters to be removed in any order, as long as they appear at the beginning. Therefore, "www." will be stripped off, and the result will be "example.com". The "com" part at the end remains untouched because .lstrip() only removes characters from the beginning of the string.

## 12. What do these print and why?

s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))

#impatien
#impatent

# In this exercise, we have a variable `s` that stores the string `'impatient'`. We then apply the `.rstrip()` method with different arguments to understand how it affects the string. The `.rstrip()` method removes characters from the **right end** of the string, but only if those characters appear in the set of characters passed as an argument. In the first case, `s.rstrip('tp')`, the method looks at the end of the string and removes any trailing characters that are either `'t'` or `'p'`. Since `'impatient'` ends with `'t'`, that character is removed. The next character, `'n'`, is not in the set `'t'` or `'p'`, so the method stops there. As a result, the output is `'impatien'`. In the second case, `s.rstrip('p')`, the method checks if the final character `'t'` is `'p'`, which it is not, so no characters are removed, and the original string `'impatient'` is returned unchanged. This exercise demonstrates how `.rstrip()` selectively removes only the matching characters from the end of a string until it encounters a character not in the specified set.

## 13. What do these print and why?

s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0"))

# Hi, world
# Hell0, W0rld!
# In this exercise, we are working with the string s = "Hello, World!" and applying the .replace() method to modify its content. In the first call, s.replace("Hello", "Hi"), the substring "Hello" is found at the beginning of the string and is replaced with "Hi", resulting in the new string "Hi, World!". In the second call, s.replace("o", "0"), the method searches for all occurrences of the lowercase letter "o" and replaces them with the digit "0". Since there are two "o" characters in "Hello, World!", one in "Hello" and one in "World", both are replaced, producing the string "Hell0, W0rld!". These examples demonstrate how the .replace() method returns a new string with all matches replaced and how strings remain immutable in Python, meaning the original string s is not changed.

## 14. What do these print and why?

sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2)
print(words)

# ['This', 'is', 'a', 'sample', 'sentence.']
# ['John', 'Doe', '30', 'New York']
# ['This', 'is', 'a sample sentence.']

# In this exercise, we work with string splitting using Python’s split() method. First, the sentence "This is a sample sentence." is split using the default whitespace separator, resulting in a list of five words: ['This', 'is', 'a', 'sample', 'sentence.']. Next, we take a string formatted like CSV data, "John,Doe,30,New York", and split it using a comma as the separator, which produces a list with four elements: ['John', 'Doe', '30', 'New York']. Finally, we again split the original sentence but this time with maxsplit=2, meaning Python will only perform two splits from the left. This gives us a list with three elements: ['This', 'is', 'a sample sentence.'], where the remaining part of the sentence after the second word stays grouped as one string.

## 15. What do these print and why?

str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)

# Original string: hello world)
# Capitalized string: Hello world)

# n this exercise, the variable str1 is assigned the string "hello world". Then, we create a new variable str2 and assign it the result of applying the capitalize() method to str1. The capitalize() method returns a copy of the string with the first character capitalized and the rest of the string in lowercase. So "hello world" becomes "Hello world". Finally, we print the original string (which is still "hello world") and the capitalized version (which is "Hello world").