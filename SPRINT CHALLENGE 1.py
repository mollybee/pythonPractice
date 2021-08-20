######SPRINT CHALLENGE 1
##########################################################################################
##### 3RD PROBLEM AND SOLUTION

#problem: Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

# Examples:

# `csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
# `csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
#sOLUTION: 

def csRemoveDuplicateWords(input_str):
    #changing the input_str into an array --> ("alpha bravo bravo") ---> ('alpha', 'bravo', 'bravo')
    wordsArray = input_str.split()
    print(wordsArray)
    
    #creating a new array to store our new array of duplicate removal
    uniqueWordsArray = []
    
    #the length of the array decreases with every
    while len(wordsArray) > 0: 
        nextWord = wordsArray.pop(0)    # Remove next word from front of array, then once it's checked, it gets removed             automatically (.pop() is doing this) from the wordsArray, and during the next iteration through the loop,                 'nextWord' is grabbing the next word in the wordsArray list --> see the below print statement checking out the            remaining words in the original wordsArray list after we do an interation.
        print("Next Word:", nextWord)
        print("Remaining Words: ", wordsArray)
        
        # If we haven't already encountered this word, add it to our array
        if nextWord not in uniqueWordsArray:
            uniqueWordsArray.append(nextWord)
            
        print("Unique Words: ", uniqueWordsArray)
    
    # Smoosh all of our unique words back together into a string, not a list, separated by a space, to create our unique        word string.
    freeFromDuplicateWordsString = ' '.join(uniqueWordsArray)
    
    return freeFromDuplicateWordsString

#OBJECTIVE: write a function that removes all duplicate words from the input string    
# ###############################################################################################
# 2ND PROBLEM AND SOLUTION
# PROBLEM:  
# A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

# Given a string, write a function that checks if the input is a valid palindrome.

# Examples:

# csCheckPalindrome("racecar") -> true
# csCheckPalindrome("anna") -> true
# csCheckPalindrome("12345") -> false
# csCheckPalindrome("12321") -> true

#SOLUTION
def csCheckPalindrome(input_str):
    
    # FOR Loop answer
    # i = len(input_str) - 1
    # for x in input_str:
    #     if x != input_str[i]:
    #         return False
    #     i -= 1
        
    # return True
    ##########
    # WHILE Loop answer
    print(input_str) #prints the full word as one string ['racecar']
    input_str_array = list(input_str) #changing input_str word ('racecar') to an array or 'list' of letters ('r', 'a', ..)
    print(input_str_array) #prints an array of strings -- each individual letter as it's own string ['r', 'a', 'c', ...]
    
    #for the length of number of items in the input_str_array
    while len(input_str_array) > 1: 
        # Remove first and last item from the array
        frontChar = input_str_array.pop(0) #removing the item from index 0
        backChar = input_str_array.pop() #removing the last index item (if no index is specified, pop takes the last                index)
        #viewing my variables - to check they're grabbing and comparing the first and last items
        print("frontChar:", frontChar)
        print("backChar:", backChar)
        print("remaining Array Items:", input_str_array)
        
        # Comparing them
        if frontChar != backChar:
            return False
    
    # Our array is either empty, or there is one character left
    # All chars matched, so we can safely return true
    return True
###################################################################################################################
# 1st PROBLEM AND SOLUTION
# PROBLEM: 
# Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

# Examples:

# csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
# csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
#SOLUTION: 

# def csReverseString(chars):
#     # what we are trying to find
#     reversedString = []
    
#     indexOfLastItemInCharsArray = len(chars) - 1
    
#     i = 0
#     while i < len(chars):
#         nextCharacterToAdd = chars[indexOfLastItemInCharsArray - i]
#         reversedString.append(nextCharacterToAdd)
#         i += 1
    
#     return reversedString
##############
#OBJECTIVE:  
# A string's input will be an array of characters

    # ex) Input: csReverseString(["l", "a", "m", "b", "d", "a"])
    #     Ouput: -> ["a", "d", "b", "m", "a", "l"]
    
#in-place meaning I should return the modified original array, not a new one

############
def csReverseString(chars):
    #reversedString = [] --> *This is modifying out-of-place
    #What we're trying to solve is: reversing the original array and returning it
    
    #loop/iterate through the array - while i is less than the length of 'chars'
    i = 0 
    while i < len(chars):
        #removed the item (as a string) at the 'i' index position, and stored it in the variable 'removedFirstItemInArray"
        removedLastItemInArray = chars.pop() # if you don't provide a position, it defaults to the last position
        print("Removing")
        print(removedLastItemInArray)
        # now take that removed item, and insert it to the next position in the array
        chars.insert(i,removedLastItemInArray)
        print(chars)
        i += 1
        
    return chars
################

## List.insert - Add an item to the end of the list (i,removedLastITemInArray) --> the position we're inserting it, and the item we removed
## List.pop([])Remove the item at the given position in the list