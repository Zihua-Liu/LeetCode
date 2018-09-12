#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (33.06%)
# Total Accepted:    136.4K
# Total Submissions: 412.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
        	return 0
        ans = len(nums) + 1
        start = 0
        subarray_sum = 0
        for end in range(0, len(nums)):
        	subarray_sum += nums[end]
        	if subarray_sum >= s:
        		while start <= end and subarray_sum >= s:
        			ans = min(ans, end - start + 1)
        			subarray_sum -= nums[start]
        			start += 1
        if ans == len(nums) + 1:
        	return 0
        else:
        	return ans
