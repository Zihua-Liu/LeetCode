#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (37.69%)
# Total Accepted:    60.1K
# Total Submissions: 159.1K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#
# 7, 7, 5,
# 2 ,4, 6, 
# 8, 2, 0
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0
        record = {}
        for i in range(0, len(matrix)):
        	for j in range(0, len(matrix[0])):
        		ans = max(ans, self.dfs(matrix, i, j, -1, [], record))
        return ans

    def dfs(self, matrix, i, j, current_height, series, record):
    	if (i, j) in series:
    		return 0
    	if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
    		return 0
    	if matrix[i][j] <= current_height:
    		return 0
    	if (i, j) in record.keys():
    		return record[(i, j)]
    	series.append((i, j))
    	result = 1 + max(self.dfs(matrix, i + 1, j, matrix[i][j], series, record)
    					, self.dfs(matrix, i - 1, j, matrix[i][j], series, record)
    					, self.dfs(matrix, i, j + 1, matrix[i][j], series, record)
    					, self.dfs(matrix, i, j - 1, matrix[i][j], series, record))
    	record[(i, j)] = result
    	series.pop()
    	return result















        
