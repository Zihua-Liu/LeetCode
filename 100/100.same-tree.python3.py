#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (47.81%)
# Total Accepted:    275.8K
# Total Submissions: 574.1K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
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
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		mid_result_p = []
		mid_result_q = []
		prev_result_p = []
		prev_result_q = []
		self.dfs_mid(p, mid_result_p)
		self.dfs_mid(q, mid_result_q)
		self.dfs_prev(p, prev_result_p)
		self.dfs_prev(q, prev_result_q)

		if mid_result_p == mid_result_q and prev_result_p == prev_result_q:
			return True 
		else:
			return False
	
	def dfs_mid(self, root, result):
		if root == None:
			result.append(None)
			return
		self.dfs_mid(root.left, result)
		result.append(root.val)
		self.dfs_mid(root.right, result)

	def dfs_prev(self, root, result):
		if root == None:
			result.append(None)
			return
		result.append(root.val)
		self.dfs_prev(root.left, result)
		self.dfs_prev(root.right, result)










		
