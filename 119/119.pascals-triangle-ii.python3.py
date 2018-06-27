#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (38.23%)
# Total Accepted:    150.3K
# Total Submissions: 387.4K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		result = []
		for i in range(rowIndex + 1):
			result.append(0)
		result[0] = 1
		for i in range(1, rowIndex + 1):
			result[i] = 1
			j = i - 1
			while j > 0:
				result[j] = result[j] + result[j - 1]
				j -= 1
		return result



