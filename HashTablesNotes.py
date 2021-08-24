########################################################################
# HASH TABLES LECTURE I 

"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).
​
You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.
​
The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".
​
Example 1:
​
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
​
Example 2:
​
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
​
Example 3:
​
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
​
Notes:
​
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def compare_words(word1, word2, order_dict):
    # return true if word1 < word2
    # go letter by letter of both words
    for i in range(min(len(word1), len(word2))):
        if word1[i] == word2[i]:
            continue
        if order_dict[word1[i]] < order_dict[word2[i]]:
            return True
        else:
            return False
    
    # Compare length
    if len(word2) < len(word1):
        return False
    
    return True
​
def are_words_sorted(words, alpha_order):
    # Build our order_dict
    order_dict = {}
    for i in range(len(alpha_order)):
        order_dict[alpha_order[i]] = i
    # loop through words
    for i in range(len(words) - 1):
        # compare curr_word to next_word
        curr_word = words[i]
        next_word = words[i + 1]
        if not compare_words(curr_word, next_word, order_dict):
            return False
    return True
​
words = ["lambda","school"] 
order = "hlabcdefgijkmnopqrstuvwxyz"
​
print(are_words_sorted(words, order))
​
words = ["lambda","lamb"] 
order = "abcdefghijklmnopqrstuvwxyz"
​
print(are_words_sorted(words, order))
​
words = ["were","where","yellow"]
order = "habcdefgijklmnopqrstuvwxyz"
​
print(are_words_sorted(words, order))


################################################################################
# HASH TABLES I LECTURE NOTES

# my_dict = {}
# my_dict = dict()
​
class HashTable:
    def __init__(self, size = 8):
        self.storage = [None] * size
​
    def hash_func(self, string):
        # Add up all the encoded values of
        # the string chars
        sum = 0
        for char in string:
            sum += ord(char)
        return sum % len(self.storage)
​
    def put(self, key, value):
        # Hash the key
        index = self.hash_func(key)
        if (self.storage[index] is not None):
            print("OH NO, collision")
            return
        # store the value
        self.storage[index] = (key, value)
​
    def get(self, key):
        # Hash the key
        index = self.hash_func(key)
        # Retreive the value
        return self.storage[index][1]
    
    def delete(self, key):
        # Hash the key
        index = self.hash_func(key)
        self.storage[index] = None
    
    def __setitem__(self, key, value):
        self.put(key, value)
​
    def __getitem__(self, key):
        return self.get(key)
​
​
my_dict = HashTable()
my_dict['apple'] = 'is a fruit'
my_dict['banana'] = 'banana is a fruit'
print(my_dict.storage)
my_dict['peach'] = 'is not a banana'
# print(my_dict.storage)
print(my_dict['banana'])
​
print(my_dict.hash_func('banana'))
print(my_dict.hash_func('peach'))

#####################################################

##ENCODING EXAMPLE
string = "Hello world"
​
char = "H"
​
print(bin(ord("H")))
print(ord("a"))
​
print([binary for binary in string.encode()])
​
print(chr(129321))

##BINARY CONVERSION EXAMPLE

# 114 To binary # 1110010
num = 114
print(bin(num))
​
# 10010110 to decimal
num = 0b10010110
print(int(num))
# 150? 
​
# 114 to HEX... Base 16 number system
#               0 - 9 A - F (16 values per digit)
# 72, 
num = 114
print(hex(num))
​
# 72 back to decimal
num = 0x72
print(num)
​
print(hex(224))
​
​
class SomeClass:
	def __init__(self):
		pass
​
new_instance = SomeClass()
​
print(new_instance)
print(id(new_instance))
print(hex(id(new_instance)))


################################################

## PIVOT INDEX EXAMPLE

"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
​
The "pivot" index is where the sum of all the numbers on the left of that index is equal 
to the sum of all the numbers on the right of that index.
​
If the input array does not have a "pivot" index, then the function should return `-1`. 
If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
​
Example 1:
​
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal 
to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
​
Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        # Remove the new value from right_sum
        right_sum -= nums[i]
        if right_sum == left_sum:
            return i
        left_sum += nums[i]
    return -1
​
print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([1]))
print(pivot_index([0, 1, 0]))
print(pivot_index([]))
​
# def pivot_index(nums):
#     for i in range(len(nums)):
#         left_sum = sum(nums[ : i])
#         right_sum = sum(nums[i + 1 : ])
#         if left_sum == right_sum:
#             return i
#     return -1
