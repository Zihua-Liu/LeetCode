#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.10%)
# Total Accepted:    189.3K
# Total Submissions: 460.7K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
        	return False
        while n != 1:
        	if n % 2 != 0:
        		return False
        	n /= 2
        return True
