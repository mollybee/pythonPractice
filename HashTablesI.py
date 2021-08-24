##HASH TABLES NOTES: 
'hash functions convert strings into indexes, then we store the string into that index in the hash array'
'HASH FUNCTION + ARRAY = HASH TABLE' 
'hashing functions operate on the individual characters making up the string'
'This being said, we can encode strings into their bytes representation with the .encode() method'
'Once you use .encode, each strings character is now represented by a number'
        #example: 

            bytes_representation = "hello".encode() #encoding each letter of 'hello' into a number

            for byte in bytes_representation: #byte is one single letter
                print(byte)

                ### Print Output
                ### 104 -- H
                ### 101 -- E
                ### 108 -- L
                ### 108 -- L
                ### 111 -- 0

'Now that we changed each letter into a number, we can manipulate them, using an accumulator pattern to add all the integers together'

        #example:
            bytes_representation = "hello".encode()

                sum = 0
                for byte in bytes_representation:
                    sum += byte #looping through each character and adding each number to the variable sum, then printing the total

                print(sum)

                ### Print Output
                ### 532 - all the numbers added together
'Great! Now the string is transformed into one giant number. We can wrap all of the logic of the last two steps, into a function:'

        #example: 
            def my_hashing_func(str): #wrapped the encoding & adding into the my_hashing_func
                bytes_representation = str.encode()

                sum = 0
                for byte in bytes_representation:
                    sum += byte

                return sum

'As shown earlier, hello returns 532. But, what if our hash table only has ten slots? We have to make 532 a number less than 10, so the value of 532 can be assigned to that index between 1 and 10.'
'We can do this by using the % modulo operator - this makes sure the summed number that the hashing function returns is within a specific range of numbers'

        #example:
            def my_hashing_func(str, table_size): #here you can pass in a table size as a parameter to be included in the function
                bytes_representation = str.encode()

                sum = 0
                for byte in bytes_representation:
                    sum += byte

                return sum % table_size # using the table_size here to change the summed integer into a number that fits into our table_size

##HASH TABLE CLASSES

'With hash tables, we can implement a user-defined hashTable class, that uses basic operations (insert, put, delete, get)'
"We start by defining a hash table as an empty array, and a hash function is a function that takes a value and converts it into an array
"index that tells you where to store that value (see above).

"So now we can put the hash table(empty array) TOGETHER with the hash function to make a HashTable Class!"
        "Insert (put) values into a hashtable" -- "Insert a value with an associated key" -- 
            #example: Let's store instructor with the place they live --> ("Parth", "California")
        "Retrieve values from a hash table"
        "Delete values from a hash table"

    
    ##Here's what our HashTable class looks like: 

        class HashTable:
            def __init__(self, size = 8):           #capacity of hashtable 
                self.storage = [None] * size
             
            def hash_func(self, string):            #our hash function -- adding up all the encoded numbers
                sum = 0
                for char in string:
                    sum += ord(char)                #we are changing each letter to a 'unicode'  integer, you can also use .encode(), then summing all the numbers
                return sum % len(self.storage)      #checking the total summed numbers against the amount of storage we have in our table

            def put(self, key, value):
                # Hash the key
                index = self.hash_func(key)
                if (self.storage[index] is not None):
                    print("OH NO, collision, there's two things at this index")
                    return
                # store the value
                self.storage[index] = (key, value)

            def get(self, key):
                # Hash the key
                index = self.hash_func(key)
                # Retreive the value
                return self.storage[index][1]
            
            def delete(self, key):
                # Hash the key
                index = self.hash_func(key)
                self.storage[index] = None
            
            def __setitem__(self, key, value): ## Adding an item to our table
                self.put(key, value)

            def __getitem__(self, key):        ## Retrieving an item from our table
                return self.get(key)

        my_dict = HashTable()       ## Setting our HashTable() to our variable Dict. We created our own dictionary of stored info!
        my_dict['apple'] = 'is a fruit'
        my_dict['banana'] = 'banana is a fruit'
        print(my_dict.storage)
        my_dict['peach'] = 'is not a banana'
        print(my_dict.storage)
        print(my_dict['banana'])
        print(my_dict.hash_func('banana'))
        print(my_dict.hash_func('peach'))











~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### 8/23 - HASH TABLES I Assignment Problems


###You are given a non-empty array of integers.
# One element appears exactly once, with every other element appearing at least twice, perhaps more.
# Write a function that can find and return the element that appears exactly once.

def csFindTheSingleNumber(nums):
#non-empty array of numbers - nums
    nonEmptyArrayOfNumbers = nums
    print("nonEmptyArrayOfNumbers:", nonEmptyArrayOfNumbers)
    # set a new empty variable containing a placeholder number
    theOneRingToRuleThemAll = 0

    #Loop through nonEmptyArrayOfNumbers
    for i in range(len(nonEmptyArrayOfNumbers)):
        # access each number one at a time in the array and compare to our return variable
        if nonEmptyArrayOfNumbers[i] == theOneRingToRuleThemAll:
            continue
        #else if !=, store that number as the 'one' number variable
        else:
            theOneRingToRuleThemAll = nonEmptyArrayOfNumbers[i]
        
    return theOneRingToRuleThemAll
        
csFindTheSingleNumber([1, 1, 2, 1]) # sUCCESS - but does not work with negative integers

#################################################################
#PROBLEM # 2
# Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.
# Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
# The average student `1` is `87`.
# The average of student `2` is `88.6`, but with integer division is `88`.

def csAverageOfTopFive(scores):


################################################################
#PROBLEM # 3

# Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.
# You can use each character in text at most once.
# Write a function that returns the maximum number of instances of "lambda" that can be formed.

# Input: text = "mbxcdatlas"
# Output: 1

def csMaxNumberOfLambdas(text):