#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (30.12%)
# Total Accepted:    80.2K
# Total Submissions: 266.4K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1 = None
        num2 = None
        count1 = 0
        count2 = 0
        for num in nums:
        	if num == num1:
        		count1 += 1
        	elif num == num2:
        		count2 += 1
        	elif count1 == 0:
        		num1 = num
        		count1 += 1
        	elif count2 == 0:
        		num2 = num
        		count2 += 1
        	else:
        		count1 -= 1
        		count2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
        	if num == num1:
        		count1 += 1
        	elif num == num2:
        		count2 += 1
        ans = []
        if count1 > len(nums) // 3:
        	ans.append(num1)
        if count2 > len(nums) // 3:
        	ans.append(num2)
        return ans
        
