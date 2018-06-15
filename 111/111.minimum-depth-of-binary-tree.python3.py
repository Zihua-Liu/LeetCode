#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (33.57%)
# Total Accepted:    221.1K
# Total Submissions: 655.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None:
			return 0
		if root.left == None and root.right == None:
			return 1
		elif root.left != None and root.right == None:
			return self.minDepth(root.left) + 1
		elif root.left == None and root.right != None:
			return self.minDepth(root.right) + 1
		else:
			return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
