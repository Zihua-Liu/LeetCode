#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (44.86%)
# Total Accepted:    241.3K
# Total Submissions: 530K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
from copy import deepcopy
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dfs(nums)
    def dfs(self, nums):
    	if len(nums) == 0:
    		return [[]]
    	res = self.dfs(deepcopy(nums[1:]))
    	result = []
    	for item in res:
    		result.append([nums[0]] + item)
    		result.append(item)
    	return result
        
