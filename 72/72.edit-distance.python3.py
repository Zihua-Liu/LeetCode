#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (32.56%)
# Total Accepted:    115.4K
# Total Submissions: 354.2K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        distance = []
        for i in range(len1 + 1):
        	array = []
        	for j in range(len2 + 1):
        		array.append(-1)
        	distance.append(array)
        distance[0][0] = 0
        for i in range(1, len1 + 1):
        	distance[i][0] = i
        for j in range(1, len2 + 1):
        	distance[0][j] = j
        for i in range(1, len1 + 1):
        	for j in range(1, len2 + 1):
        		distance[i][j] = distance[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
        		distance[i][j] = min(distance[i][j], distance[i - 1][j] + 1)
        		distance[i][j] = min(distance[i][j], distance[i][j - 1] + 1)
        return distance[len1][len2]
        
