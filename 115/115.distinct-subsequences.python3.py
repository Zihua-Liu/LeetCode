#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (32.93%)
# Total Accepted:    89.2K
# Total Submissions: 270.7K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# Example 1:
# 
# 
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# 
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
# 
# Example 2:
# 
# 
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# 
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
# 
# 
#
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        f = []
        for i in range(0, len(s) + 1):
        	f.append([1])
        	for j in range(1, len(t) + 1):
        		f[i].append(0)

        for i in range(1, len(s) + 1):
        	for j in range(1, len(t) + 1):
        		if s[i - 1] == t[j - 1]:
        			f[i][j] = f[i - 1][j] + f[i - 1][j - 1]
        		else:
        			f[i][j] = f[i - 1][j]
        return f[len(s)][len(t)]

        
