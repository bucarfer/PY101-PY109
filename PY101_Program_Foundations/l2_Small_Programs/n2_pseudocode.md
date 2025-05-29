Write out pseudocode (both casual and formal) that does the following:

1. A function that returns the sum of two numbers
START 
GET retrieve numbers from user
SET result = num1 + num2
RETURN result 
END

2. A function that takes a list of strings, and returns a string that is all those strings concatenated together
START 
# Given a list of strings called "strings"
SET result = empty string

For each string in strings
    result = result + string 

RETURN result
END

3. A function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance: every_other([1,4,7,2,5]) # => [1,7,5]
START
# Given a list of integers called "integers"
SET result = empty list
SET index = 0

WHILE index < length of integers
    IF index % 2 == 0
        APPEND integers[index] to result 
    INCREMENT index by 1
    END IF 
END WHILE

RETURN result 
END 

4. A function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.
START
# Given a string and a character 
SET count = 0
SET index = 0

WHILE index < length of string
    IF string[index] == character 
        INCREMENT count by 1
        IF COUNT == 3
            RETURN index
        END IF
    END IF
    INCREMENT index by 1
END WHILE

RETURN None 
END 

5. A function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:
Copy Code - merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
You may assume that both list arguments have the same number of elements.

START 
# Given two lists of numbers with same length
SET list1
SET list2
SET result = empty list
SET index = 0

WHILE index < length of list 
    APPEND list1[index] to result
    APPEND list2[index] to result
    INCREMENT index by 1
END WHILE

RETURN result
END 

