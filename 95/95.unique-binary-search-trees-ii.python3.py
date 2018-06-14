#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (32.30%)
# Total Accepted:    104.6K
# Total Submissions: 321.1K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution:
	def generateTrees(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		if n == 0:
			return []
		series_list = []
		self.generateSeries(0, n, [], series_list)
		print(series_list)
		result = []
		record = []
		for series in series_list:
			tree = self.constructBST(series)
			record_series = []
			self.dfs(tree, record_series)
			if record_series not in record:
				record.append(record_series)
				result.append(tree)
		return result


	def generateSeries(self, k, n, series, result):
		if k == n:
			result.append(copy.deepcopy(series))
			return
		for i in range(1, n + 1):
			if i not in series:
				series.append(i)
				self.generateSeries(k + 1, n, series, result)
				series.pop()
		return

	def constructBST(self, series):
		root = TreeNode(series[0])
		for i in range(1, len(series)):
			self.insert_BST(root, series[i])
		return root

	def insert_BST(self, root, val):
		if val < root.val:
			if root.left == None:
				root.left = TreeNode(val)
				return
			else:
				self.insert_BST(root.left, val)
		elif val > root.val:
			if root.right == None:
				root.right = TreeNode(val)
				return
			else:
				self.insert_BST(root.right, val)

	def dfs(self, root, result):
		if root == None:
			return
		result.append(root.val)
		self.dfs(root.left, result)
		self.dfs(root.right, result)
sol = Solution()
sol.generateTrees(3)



		
