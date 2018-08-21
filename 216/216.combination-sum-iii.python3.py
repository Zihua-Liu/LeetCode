#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (48.38%)
# Total Accepted:    97.2K
# Total Submissions: 200.8K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
# 
#
import copy
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(k, n, [], result)
        return result
    
    def dfs(self, k, n, series, result):
    	if k == 0 and n == 0:
    		if series not in result:
    			result.append(copy.deepcopy(series))
    	if k == 0 or n == 0:
    		return
    	for i in range(1, 10):
    		if i not in series:
    			if series != [] and i < series[-1]:
    				continue
    			series.append(i)
    			self.dfs(k - 1, n - i, series, result)
    			series.pop()
    	return
