#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.77%)
# Total Accepted:    237K
# Total Submissions: 595.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
# 
#
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        digits[-1] += 1
        for i in range(0, len(digits)):
        	if digits[-1 - i] < 10:
        		result.append(digits[-1 - i])
        	else:
        		result.append(digits[-1 - i] % 10)
        		if i != len(digits) - 1:
        			digits[-2 - i] += 1
        		else:
        			result.append(1)
        final_result = []
        for i in range(len(result)):
        	final_result.append(result[-1 - i])
        return final_result


        
