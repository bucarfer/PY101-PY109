### 1. Original code
# def titlize(sentence):
#     words = sentence.split()
#     new_words = []

#     for word in words:
#         if len(word) > 2:
#             word.capitalize()
#             new_words.append(word)

#     return ' '.join(new_words)

# title = 'hello world of programming'
# print(titlize(title))

### 2. Debug with Print

# def titlize(sentence):
#     words = sentence.split()
#     print(words) # 1. we should see words separated
#     new_words = []

#     for word in words:
#         print(word) # 2. print words one by one
#         if len(word) > 2:
#             print(word) #3. check if statement (does not include of)
#             word.capitalize()
#             print(word) #4. check capitalization works (it does not, word is a string and it is immutable, we need a reassignment)
#             new_words.append(word)
#         print(new_words) #5. check for loop and if all words are append

#     return ' '.join(new_words)
# title = 'hello world of programming'
#print(titlize(title))

### 3. New version of code with amendments in lines 25 and 28:

def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize() # 1. reassign words to capitalize

        new_words.append(word) #2. Move .append outside if loop and inside for loop to include all words
    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))

# Solution: "Hello World of Programming"