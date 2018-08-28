#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (30.97%)
# Total Accepted:    98.3K
# Total Submissions: 316.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
# 
#
import copy
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
        	return 0
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		matrix[i][j] = int(matrix[i][j])
        length = 0
        record = copy.deepcopy(matrix)
        for l in range(1, min(len(matrix), len(matrix[0])) + 1):
        	find = False
        	for i in range(l - 1, len(matrix)):
        		for j in range(l - 1, len(matrix[0])):
        			if l == 1:
        				if int(matrix[i][j]) == 1:
        					length = 1
        					find = True
        			else:
	        			if matrix[i][j] >= 1 and matrix[i - 1][j] == l - 1 and matrix[i][j - 1] == l - 1 and matrix[i - l + 1][j - l + 1] >= 1:
	        				record[i][j] = l
	        				length = l
	        				find = True
        	if find == False:
        		return length * length
        	else:
        		matrix = copy.deepcopy(record)
        return length * length
sol = Solution()
print(sol.maximalSquare([["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]))
        
