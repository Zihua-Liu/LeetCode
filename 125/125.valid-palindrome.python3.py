#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (27.70%)
# Total Accepted:    241.1K
# Total Submissions: 870.3K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
        	left_str = s[i:i+1]
        	right_str = s[j:j+1]
        	if not (left_str.isalpha() or left_str.isdigit()):
        		i += 1
        		continue
        	if not (right_str.isalpha() or right_str.isdigit()):
        		j -= 1
        		continue
        	if left_str.upper() != right_str.upper():
        		return False 
        	else:
        		i += 1
        		j -= 1
        return True
        
