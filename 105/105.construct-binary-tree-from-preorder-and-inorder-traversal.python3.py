#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (34.24%)
# Total Accepted:    146.8K
# Total Submissions: 419.6K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def buildTree(self, preorder, inorder):
		"""
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""
		if len(preorder) == 0:
			return None
		root_val = preorder[0]
		root_index = inorder.index(root_val)
		left_inorder = inorder[0:root_index]
		right_inorder = inorder[root_index + 1:]
		left_preorder = preorder[1: 1 + len(left_inorder)]
		right_preorder = preorder[1 + len(left_inorder):]
		root = TreeNode(root_val)
		root.left = self.buildTree(left_preorder, left_inorder)
		root.right = self.buildTree(right_preorder, right_inorder)
		return root


		
