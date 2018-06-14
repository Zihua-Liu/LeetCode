#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (49.82%)
# Total Accepted:    295.9K
# Total Submissions: 584K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result = []
		self.dfs(root, result)
		return result
	
	def dfs(self, root, result):
		if root == None:
			return
		self.dfs(root.left, result)
		result.append(root.val)
		self.dfs(root.right, result)
