#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.64%)
# Total Accepted:    157.1K
# Total Submissions: 453.4K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#
class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		return self.binarySearch(0, len(matrix) * len(matrix[0]) - 1, matrix, len(matrix), len(matrix[0]), target)
	def array_to_matrix(self, matrix, index, row_cnt, col_cnt):
		row = int(index / col_cnt)
		col = int(index % col_cnt)
		return matrix[row][col]


	def binarySearch(self, left, right, matrix, row_cnt, col_cnt, target):
		if left == right:
			value = self.array_to_matrix(matrix, left, row_cnt, col_cnt)
			if value == target:
				return True
			else:
				return False

		mid = int((left + right) / 2)
		print(str(left) + " " + str(mid) + " " + str(right))
		value = self.array_to_matrix(matrix, mid, row_cnt, col_cnt)
		if value == target:
			return True
		elif value < target:
			return self.binarySearch(mid + 1, right, matrix, row_cnt, col_cnt, target)
		elif value > target:
			return self.binarySearch(left, mid, matrix, row_cnt, col_cnt, target)











		
