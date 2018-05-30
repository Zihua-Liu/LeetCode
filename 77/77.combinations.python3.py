#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (41.34%)
# Total Accepted:    146.9K
# Total Submissions: 351.3K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
from copy import deepcopy
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(1, n + 1):
        	arr.append(i)
        return self.dfs(arr, k)

    def dfs(self, arr, k):
    	if k == 0:
    		return [[]]
    	if len(arr) == k:
    		return [arr]
    	res1 = self.dfs(deepcopy(arr[1:]), k - 1)
    	res2 = self.dfs(deepcopy(arr[1:]), k)
    	result = []
    	for item in res1:
    		result.append([arr[0]] + item)
    	for item in res2:
    		result.append(item)
    	return result

        
