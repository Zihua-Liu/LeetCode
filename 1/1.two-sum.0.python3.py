#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (38.72%)
# Total Accepted:    1M
# Total Submissions: 2.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_set = {}
        for i in range(len(nums)):
        	num1 = nums[i]
        	num2 = target - num1
        	if num2 in hash_set.keys():
        		return [i, hash_set[num2]]
        	else:
        		hash_set[num1] = i
        return []
        
