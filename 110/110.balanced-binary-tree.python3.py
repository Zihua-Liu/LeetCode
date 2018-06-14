#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (38.46%)
# Total Accepted:    233.3K
# Total Submissions: 602.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[1]
    def dfs(self, root):
    	if root == None:
    		return (0, True)
    	left = self.dfs(root.left)
    	right = self.dfs(root.right)
    	depth = max(left[0], right[0]) + 1
    	valid = left[1] and right[1] and abs(left[0] - right[0]) <= 1
    	return (depth, valid)
        
