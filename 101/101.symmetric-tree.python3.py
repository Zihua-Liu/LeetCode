#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (40.45%)
# Total Accepted:    263.2K
# Total Submissions: 645.9K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		left_result = []
		right_result = []
		self.dfs_left(root, left_result)
		self.dfs_right(root, right_result)
		if left_result == right_result:
			return True 
		else:
			return False


	def dfs_left(self, root, result):
		if root == None:
			result.append(None)
			return
		result.append(root.val)
		self.dfs_left(root.left, result)
		self.dfs_left(root.right, result)

	def dfs_right(self, root, result):
		if root == None:
			result.append(None)
			return
		result.append(root.val)
		self.dfs_right(root.right, result)
		self.dfs_right(root.left, result)
		
