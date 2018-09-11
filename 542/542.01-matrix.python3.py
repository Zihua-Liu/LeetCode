#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (33.49%)
# Total Accepted:    27K
# Total Submissions: 80.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# Example 1: 
# Input:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 
# Example 2: 
# Input:
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 
# Note:
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
# 
#
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        record = [[-1] * len(matrix[i]) for i in range(len(matrix))]
        queue = []
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		if matrix[i][j] == 0:
        			record[i][j] = 0
        			queue.append((i, j))

        while queue != []:
        	top = queue[0]
        	queue.pop(0)
        	i, j = top[0], top[1]
        	if i > 0 and record[i - 1][j] == -1:
        		record[i - 1][j] = 1 + record[i][j]
        		queue.append((i - 1, j))
        	if i < len(matrix) - 1 and record[i + 1][j] == -1:
        		record[i + 1][j] = 1 + record[i][j]
        		queue.append((i + 1, j))
        	if j > 0 and record[i][j - 1] == -1:
        		record[i][j - 1] = 1 + record[i][j]
        		queue.append((i, j - 1))
        	if j < len(matrix[i]) - 1 and record[i][j + 1] == -1:
        		record[i][j + 1] = 1 + record[i][j]
        		queue.append((i, j + 1))
        return record

        
