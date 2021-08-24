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