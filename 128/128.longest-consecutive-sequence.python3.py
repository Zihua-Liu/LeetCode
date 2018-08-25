#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (39.04%)
# Total Accepted:    156.5K
# Total Submissions: 400.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set_start = {}
        hash_set_end = {}
        ans = 0
        for num in nums:
        	left = hash_set_end[num - 1] if num - 1 in hash_set_end.keys() else 0
        	right = hash_set_start[num + 1] if num + 1 in hash_set_start.keys() else 0
        	if num - left not in hash_set_start.keys():
        		hash_set_start[num - left] = 0
        	if num + right not in hash_set_end.keys():
        		hash_set_end[num + right] = 0
        	hash_set_start[num - left] = max(hash_set_start[num - left], left + right + 1)
        	hash_set_end[num + right] = max(hash_set_end[num + right], left + right + 1)
        	ans = max(ans, left + right + 1)
        return ans
        
