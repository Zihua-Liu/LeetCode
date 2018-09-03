#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (47.49%)
# Total Accepted:    165K
# Total Submissions: 347.4K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
# 
# Note:
# 
# 
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Example:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
#
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_set = {}
        for i in range(len(numbers)):
        	if target - numbers[i] in hash_set.keys():
        		return [hash_set[target - numbers[i]] + 1, i + 1]
        	hash_set[numbers[i]] = i
        return None
        
