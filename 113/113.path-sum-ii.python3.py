#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (35.74%)
# Total Accepted:    169.6K
# Total Submissions: 467.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		result = []
		self.dfs(root, sum, result, [])
		return result

	def dfs(self, root, sum, result, series): 
		if root == None:
			return
		if root.val == sum and root.left == None and root.right == None:
			series.append(root.val)
			result.append(copy.deepcopy(series))
			series.pop()
			return
		series.append(root.val)
		self.dfs(root.left, sum - root.val, result, series)
		self.dfs(root.right, sum - root.val, result, series)
		series.pop()
		return
		
		
