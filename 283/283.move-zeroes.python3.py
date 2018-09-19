#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (52.35%)
# Total Accepted:    342.9K
# Total Submissions: 654.9K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# 
#
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
        	if nums[i] == 0:
        		j = i + 1
        		while j < len(nums) and nums[j] == 0:
        			j += 1
        		if j == len(nums):
        			break
        		nums[i], nums[j] = nums[j], 0
        return
        
