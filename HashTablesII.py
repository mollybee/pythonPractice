# HASH TABLES II ASSIGNMENTS 8 - 24

############################################################
##PROBLEM #1
# Given two strings a and b, determine if they are isomorphic.
# Two strings are isomorphic if the characters in a can be replaced to get b.
# All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Input: 
# a = "odd"
# b = "egg"

# Output:
# true

#def csIsomorphicStrings(a, b):

##############################################################
##PROBLEM #2

# Given a pattern and a string a, find if a follows the same pattern.
# Here, to "follow" means a full match, such that there is a one-to-one 
# correspondence between a letter in pattern and a non-empty word in 'a'

# Input:
# pattern = "abba"
# a = "lambda school school lambda"

# Output: true

#def csWordPattern(pattern, a):

#################################################################
##PROBLEM #3

# Given an array of strings strs, write a function that can group the anagrams. 
# The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Input:
# strs = ["apt","pat","ear","tap","are","arm"]

# Output:
# [["apt","pat","tap"],["ear","are"],["arm"]] 

#def csGroupAnagrams(strs):


###############################################################

##NOTES: CALCULATING LOAD_FACTOR AND RESIZING THE TABLE

"Load Factor = Number of Items in Hash Table / Total Number of Slots"

"** The load factor of a hash table is easy to calculate (see above). A hash table uses an array for storage. So an array of length 10," 
"with three items in it has a load factor of 0.3. As the load factor of your hash table increases, so does likelihood of collision,"
"which reduces your tables performance. So you need to watch your load factor and resize your hash table when the load factor gets"
"too big." 

"** The general rule of thumb is to resize your hash table when your load factor becomes greater than 0.7, and when you resize it"
"is common to double the size of the table."

"** When you resize the array, you have to re-insert all the items into the new table, by rerunning each item through the hashing function."

"** If the table is too big for the data (too small of a load factor), then memory is being wasted, and also requires resizing."
"** Good practice to resize your hash table whenever an item is inserted or deleted into the hash table."

"We added a get_load_factor and resize method to calculate the load factor and resize the hash table with a new capacity when necessary."

## EXAMPLE with 'get_load_factor' and 'resize' methods included in the hash table - incomplete hash table -- only the methods and 'put' is there to see how to resize the table

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
 

    def __init__(self, capacity):
        self.capacity = capacity  
        self.storage = [None] * capacity
        self.item_count = 0



    def get_load_factor(self):
        #the load factor equation
        return self.item_count / self.capacity

    def resize(self, new_capacity):
        # Changes the capacity of the hash table and
        # rehashes all key/value pairs.
        # Implement this.
        
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        current_entry = None

        

    def put(self, key, value):
        
        # Store the value with the given key.
        # Hash collisions should be handled with Linked List Chaining.
        # Implement this.
        
        index = self.hash_index(key)

        current_entry = self.storage[index]

        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next

        if current_entry is not None:
            current_entry.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry

            self.item_count += 1 ## to know when to resize, we need to correctly increment the count whenever we insert, or delete something

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2) # This is our get_load_factor function, that if the size of the table is greater than 0.7, we double our capacity

# Lecture Notes

#Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# ​
# ```plaintext
# Input:
# "free"
# ​
# Output:
# "eefr"
# ​
# Explanation:
# 'e' appears twice while 'f' and 'r' appear once.
# So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
# ```
# ​
# Example 2:
# ​
# ```plaintext
# Input:
# "dddbbb"
# ​
# Output:
# "dddbbb"
# ​
# Explanation:
# Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
# Note that "dbdbdb" is incorrect, as the same characters must be together.
# ```
# ​
# Example 3:
# ​
# ```plaintext
# Input:
# "Bbcc"
# ​
# Output:
# "ccBb"
# ​
# Explanation:
# "ccbB" is also a valid answer, but "Bbcc" is incorrect.
# Note that 'B' and 'b' are treated as two different characters.
# ```
# """
def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str
​
    Output:
    str
    """
    # Build our frequency_dict
    freq_dict = {}
    for char in s:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1

    output_str = "".join(sorted(s, key=lambda x : freq_dict[x], reverse=True))
    return output_str

s = 'freeabbb'
print(frequency_sort(s))

#### HASH TABLES EXAMPLE #######################################################################################
my_dict = {}
my_dict = dict()

class HashTable:
    def __init__(self, size = 8):
        self.storage = [None] * size
        self.item_count = 0

    def hash_func(self, string):
        # Add up all the encoded values of
        # the string chars
        sum = 0
        for char in string:
            sum += ord(char)
        return sum % len(self.storage)

    def load_factor(self):
        return self.item_count / len(self.storage)

    def put(self, key, value):
        # Hash the key
        index = self.hash_func(key)

        # check if self.storage at index, is None and store our value
        if self.storage[index] is None:
            self.storage[index] = [[key, value]]
            self.item_count += 1
            self.resize()
            return
        # Check if the key / value already exists
        # loop through the "collision array"
        for item in self.storage[index]:
            # compare the item key, to our current key
            if item[0] == key:
                # Update the item value
                item[1] = value
                return
        
        # We definitely have a collision, because we passed the collision check above
        self.storage[index].append([key, value])
        self.item_count += 1
        self.resize() #run the resize function to check if we need to resize


    def get(self, key):
        # Hash the key
        index = self.hash_func(key)
        # if inner array does not exist, return None
        if self.storage[index] is None:
            print("Key does not exist")
            return
        # search for our key
        for item in self.storage[index]:
            # compare the item key, to our current key
            if item[0] == key:
                # return the value
                return item[1]
        print("Key does not exist")
        
    def resize(self):
        # Check if we actually should resize
        if self.load_factor() < 0.7:
            # we don't need to resize
            return

        # Lets resize our array
        old_storage = self.storage
        self.storage = [None] * (len(old_storage) * 2) #so we're multiplying the size of the array previously by 2
        self.item_count = 0
        # Go through ALL slots in old storage, and rehash everything!
        for slot in old_storage:
            # loop over items in the slots
            if slot is None:
                continue
            for item in slot:
                key = item[0]
                value = item[1]
                self.put(key, value)
        

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


my_dict = HashTable(8)
my_dict['apple'] = 'is a fruit'
my_dict['banana'] = 'banana is a fruit'
my_dict['peach'] = 'is not a banana'
my_dict['tomato'] = 'is red'
my_dict['cucumber'] = 'is green'
my_dict['plum'] = 'is great!'
print(len(my_dict.storage))
print(my_dict.load_factor())
print(my_dict['banana'])
# print(my_dict['apple'])
# print(my_dict['peach'])
# print(my_dict.storage)
# print(my_dict.load_factor())
