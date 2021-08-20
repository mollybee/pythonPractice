def csReverseIntegerBits(n):
    #take n (an integer) and convert that number into binary
    
    # reverse the binary number
    
    #conver that reversed binary number back into an integer
    
    #return that integer
 
    csReverseIntegerBits(417)



# Input: csReverseIntegerBits(417) 
    # 417 is 110100001 in binary
    # the binary reverse if 100001011, which outputs the integer 417
# Output: 267

#Completed
def csReverseIntegerBits(n):
    num = (bin(n))
    num_as_list = list(num)
    
    reversedBinary = []
    indexOfLastItemInArray = len(num_as_list) -1
    
    i = 0
    while i < len(num_as_list):
        nextItemToAdd = num_as_list[indexOfLastItemInArray - i]
        print(nextItemToAdd)
        reversedBinary.insert(i, nextItemToAdd)
        i += 1 
    reversedBinary.pop()
    reversedBinary.pop() 
    completelyReversedArray = ''.join(reversedBinary)
    result = int(completelyReversedArray, 2)
    
    return result
csReverseIntegerBits(417)

#### NOTES 
# def csReverseIntegerBits(n):
#     #take n (an integer) and convert that number into binary
#     num = (bin(n)) #Can see it printing the binary translation stored in the num variable in the console - SUCCESS
#     print(num)
#     # reverse the binary number
#     # Step 1: first make it into a string of individual integers
#     num_as_list = list(num)
#     print(num_as_list) #Success - created list of the single binary number and stored in new variable
#     # Step 2: Create a loop, loop through it, until the number is reversed
#     reversedBinary = [] #To modify out of place
#     indexOfLastItemInArray = len(num_as_list) -1 #this never changes with the iterations, it's always 10 - the length of        the original array
#     print(indexOfLastItemInArray) #printing '10' as the last index position - success
    
#     i = 0 #As this increments, you are subtracting 10 by this number (see below) to access the original array backwards
#     while i < len(num_as_list):
#         #Looping through and grabbing each individual character, taking it off the array and putting in our new 'reversed           string' - by grabbing each item in the last in reverse and putting it starting at index 0 into the new array
#         nextItemToAdd = num_as_list[indexOfLastItemInArray - i]
#         print(nextItemToAdd)
#         reversedBinary.insert(i, nextItemToAdd)
#         #print(reversedBinary) #Successfully reversed the string into the new variable
#         i += 1
    
#     #convert that reversed binary number back into an integer -- but you need to take off the '0b' from the beginning, because now it's at the end of the array which will prevent the int() function from working 
#     reversedBinary.pop() #removing the last item on the array
#     reversedBinary.pop() #removing the last item on the array again
#     completelyReversedArray = ''.join(reversedBinary)
#     print('reversedArray', completelyReversedArray) #Success - This turned the array of strings back into one string of numbers
#     #return that reversed binary string number as an integer
    
#     # EXAMPLE: print(int(bin_a, 2)) #Base 2(binary)

#     result = int(completelyReversedArray, 2)
#     print("Result: ", result)

#     return result
# csReverseIntegerBits(417)

#############################################################################################

def csBinaryToASCII(binary):

    #take in a binary 
    
    #translate that binary into ASCII numbers ex) 01100001 --> 97

    
    #translate that ASCII number into a character --> 'a'
    
    #return that character



    csBinaryToASCII("01100001")

#Input: a binary string --> ("011011000110000101101101011000100110010001100001")
#Output: the decoded character (ASCII) --> "lambda"
###
# The input string will always be a valid binary string.
# Characters can be in the range from "00000000" to "11111111" (inclusive).
# In the case of an empty input string, your function should return an empty string.

##COMPLETED: 
def csBinaryToASCII(binary):
    binaryNum = binary
    #take in a binary 
    
    n = 8 
    #Split string for every 8-bits - using list comprehension
    split_binary_num = [binaryNum[index : index + n] for index in range(0, len(binaryNum), n)]
    
    #Access each individual index of 8-bit and change binary into decimal
    newWordArray = []
    i = 0
    while i < len(split_binary_num):
        #translate binary 8-bit into decimal
        singleDecimalString = int(split_binary_num[i], 2)
        
        #translate that 8-bit ASCII number into a character
        singleCharacterString = chr(singleDecimalString)
        
        #insert each character as a string into the new array
        newWordArray.insert(i, singleCharacterString)
        i += 1 
        
        print(newWordArray)
    
    completedWordDecoded = ''.join(newWordArray)
    return completedWordDecoded
 

csBinaryToASCII("011011000110000101101101011000100110010001100001")

#############################################################################################

def csRaindrops(number):
    #Create an empty result_string to collect the 'raindrop' sounds
    #Take in a number 
    #Use the Modulo operator to test a numbers factoring into 3, 5, or 7
    #If it IS a factor --> add the appropriate word to the result_string given 3, 5, or 7
    #Else, if it is NOT a factor of 3, 5, or 7, the result should just be the input number
    
    #return the result_string
    
    

csRaindrops(5)


#Input: an integer --> 5
#Output: a string --> "Plang"

## has 3 as a factor, add "Pling" to the result.
# has 5 as a factor, add "Plang" to the result.
# has 7 as a factor, add "Plong" to the result.
# does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.

# *Use the Modulo operator  to test is a number is a factor of another