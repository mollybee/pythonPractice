def mutateTheArray(n, a):
i = 0




mutateTheArray(n, a) = [4, 5, -1, 2, 1]
##INPUT
#n = 5
#a = [4, 5, -1, 2, 1]

##OUTPUT


#when it mutates into b, the length is still n
#for each iteration through the length of the array --> b[i] = a[i - 1] + a[i] + a[i + 1]

# Given an integer n and an array a of length n, your task is to apply the following mutation to a:

# Array a mutates into a new array b of length n.
# For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
# Example

# For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the resulting array after the mutation will be [4, 5, -1, 2, 1].


#############################################################################################################

# You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

# NOTE: + refers to string concatenation.

# Example

# For s = "xzxzx", the output should be countWaysToSplit(s) = 5.

# Consider all the ways to split s into three non-empty parts:

# If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
# If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
# If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
# If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
# If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
# If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
# Since there are five valid ways to split s, the answer is 5.

def countWaysToSplit(s):

#################################################################################################################
# You are given three arrays of integers a, b, and c. Your task is to find the longest contiguous subarray of a containing only elements that appear in b but do not appear in c.

# Return this longest subarray. If there is more than one longest subarray satisfying these conditions, return any of these possible subarrays.

# Example

# For a = [2, 1, 7, 1, 1, 5, 3, 5, 2, 1, 1, 1], b = [1, 3, 5], and c = [2, 3], the output can be longestInversionalSubarray(a, b, c) = [1, 1, 5].

# There is no contiguous subarray of length 4 satisfying all the requirements:

# a[0..3] = [2, 1, 7, 1] contains the number a[2] = 7, which doesn't appear in b;
# a[1..4] = [1, 7, 1, 1] contains the number a[2] = 7, which doesn't appear in b;
# a[2..5] = [7, 1, 1, 5] contains the number a[2] = 7, which doesn't appear in b;
# a[3..6] = [1, 1, 5, 3] contains the number a[6] = 3, which does appear in c (which is prohibited);
# a[4..7] = [1, 5, 3, 5] contains the number a[6] = 3, which does appear in c;
# a[5..8] = [5, 3, 5, 2] contains the number a[6] = 3, which does appear in c;
# a[6..9] = [3, 5, 2, 1] contains the number a[6] = 3, which does appear in c;
# a[7..10] = [5, 2, 1, 1] contains the number a[8] = 2, which doesn't appear in b;
# a[8..11] = [2, 1, 1, 1] contains the number a[8] = 2, which doesn't appear in b.
# There are two possible contiguous subarrays of length 3 satisfying all the requirements:

# a[3..5] = [1, 1, 5]: both numbers 1 and 5 appear in b, and both of these numbers don't appear in c.
# a[9..11] = [1, 1, 1]: the number 1 appears in b, and doesn't appear in c.
# example

# As you can see, the longest consecutive subarrays of a that fulfill the conditions are a[3..5] = [1, 1, 5] and a[9..11] = [1, 1, 1]. Both of these answers are acceptable.

# For a = [1, 2, 3], b = [], and c = [], the output should be longestInversionalSubarray(a, b, c) = [].

# Since b is empty, there are no elements that appear in b and not c. So the answer is [].

def longestInversionalSubarray(a, b, c):