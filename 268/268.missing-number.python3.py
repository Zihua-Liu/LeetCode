#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (46.07%)
# Total Accepted:    203.6K
# Total Submissions: 441.8K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
# 
#
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums.append(-1)
        while i < len(nums):
        	if nums[i] == -1:
        		i += 1
        		continue
        	if i != nums[i]:
        		tmp = nums[i]
        		nums[i] = nums[nums[i]]
        		nums[tmp] = tmp
        	else:
        		i += 1
        for i in range(len(nums)):
        	if nums[i] == -1:
        		return i
sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))

        
