#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (33.72%)
# Total Accepted:    111.9K
# Total Submissions: 325.8K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		if len(inorder) == 0:
			return None
		root_val = postorder[-1]
		root_index = inorder.index(root_val)
		left_inorder = inorder[0:root_index]
		right_inorder = inorder[root_index + 1:]
		left_postorder = postorder[0: len(left_inorder)]
		right_postorder = postorder[len(left_inorder):-1]
		root = TreeNode(root_val)
		root.left = self.buildTree(left_inorder, left_postorder)
		root.right = self.buildTree(right_inorder, right_postorder)
		return root
		
