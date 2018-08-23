#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (41.89%)
# Total Accepted:    29.4K
# Total Submissions: 70.1K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = {0:-1}
        diff = 0
        result = 0
        for i in range(len(nums)):
        	if nums[i] == 1:
        		diff += 1
        	else:
        		diff -= 1

        	if diff in hash_set.keys():
        		result = max(result, i - hash_set[diff])
        	else:
        		hash_set[diff] = i
        return result


        
