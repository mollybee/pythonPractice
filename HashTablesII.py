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

def csIsomorphicStrings(a, b):

##############################################################
##PROBLEM #2

# Given a pattern and a string a, find if a follows the same pattern.
# Here, to "follow" means a full match, such that there is a one-to-one 
# correspondence between a letter in pattern and a non-empty word in 'a'

# Input:
# pattern = "abba"
# a = "lambda school school lambda"

# Output: true

def csWordPattern(pattern, a):

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

def csGroupAnagrams(strs):
