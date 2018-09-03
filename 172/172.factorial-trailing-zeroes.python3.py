#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.01%)
# Total Accepted:    128.9K
# Total Submissions: 348.4K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#
import math
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        current_num = 5
        cnt_5 = 0
        while current_num <= n:
        	cnt_5 += (n // current_num)
        	current_num *= 5
        return cnt_5
