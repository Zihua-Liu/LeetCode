#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (54.43%)
# Total Accepted:    89.7K
# Total Submissions: 164.8K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
# 
#
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sum = 0
        for num in nums:
        	nums_sum ^= num
        pos = nums_sum & -nums_sum
        ans = [0, 0]
        for num in nums:
        	if num & pos:
        		ans[0] ^= num
        	else:
        		ans[1] ^= num
        return ans
        
