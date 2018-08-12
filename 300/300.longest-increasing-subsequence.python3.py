#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (39.06%)
# Total Accepted:    143.3K
# Total Submissions: 366.4K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        record_array = [1] # record[i]代表从nums[0]到nums[i]，且必须包含nums[i]的最长递增子序列
        for i in range(1, len(nums)):
            current_length = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if 1 + record_array[j] > current_length:
                        current_length = 1 + record_array[j]
            record_array.append(current_length)
        return max(record_array)























