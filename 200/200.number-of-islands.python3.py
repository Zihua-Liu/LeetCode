#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (37.81%)
# Total Accepted:    211.9K
# Total Submissions: 560.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
# 
#
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
        	return 0
        record = []
        for i in range(len(grid)):
        	record.append([])
        	for j in range(len(grid[i])):
        		record[i].append(False)

        ans = 0
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if record[i][j] == False and grid[i][j] == "1":
        			print(ans)
        			ans += 1
        			self.dfs(grid, record, i, j)
        return ans


    def dfs(self, grid, record, i, j):
    	if i < 0 or i >= len(grid):
    		return
    	if j < 0 or j >= len(grid[0]):
    		return
    	if grid[i][j] == "0":
    		return
    	if record[i][j] == True:
    		return
    	record[i][j] = True
    	self.dfs(grid, record, i - 1, j)
    	self.dfs(grid, record, i + 1, j)
    	self.dfs(grid, record, i, j - 1)
    	self.dfs(grid, record, i, j + 1)
sol = Solution()
sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])

