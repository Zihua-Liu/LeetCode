#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (49.60%)
# Total Accepted:    183.5K
# Total Submissions: 370K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
# 
#
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for letter in list(s):
        	ans *= 26
        	ans += (1 + ord(letter) - ord('A'))
        return ans
        
