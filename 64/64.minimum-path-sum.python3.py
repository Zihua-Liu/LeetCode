#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (40.85%)
# Total Accepted:    147.5K
# Total Submissions: 361K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        records = []
        for i in range(len(grid)):
        	records.append([])
        	for j in range(len(grid[i])):
        		records[i].append(-1)
        return self.dfs(grid, records, 0, 0, len(grid) - 1, len(grid[0]) - 1)

    def dfs(self, grid, records, x, y, m, n):
    	if records[x][y] != -1:
    		return records[x][y]

    	if x == m and y == n:
    		records[x][y] = grid[x][y]
    		return records[x][y]

    	if x == m:
    		records[x][y] = grid[x][y] + self.dfs(grid, records, x, y + 1, m, n)
    		return records[x][y]


    	if y == n:
    		records[x][y] = grid[x][y] + self.dfs(grid, records, x + 1, y, m, n)
    		return records[x][y]

    	records[x][y] = grid[x][y] + min(self.dfs(grid, records, x, y + 1, m, n), self.dfs(grid, records, x + 1, y, m, n))
    	return records[x][y]


















        
