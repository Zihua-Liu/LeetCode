#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (36.51%)
# Total Accepted:    137.9K
# Total Submissions: 377.3K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution:
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		zero_row = []
		zero_col = []
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 0:
					if j not in zero_col:
						zero_col.append(j)
					if i not in zero_row:
						zero_row.append(i)

		for row in zero_row:
			for j in range(len(matrix[0])):
				matrix[row][j] = 0
		for col in zero_col:
			for i in range(len(matrix)):
				matrix[i][col] = 0

		
