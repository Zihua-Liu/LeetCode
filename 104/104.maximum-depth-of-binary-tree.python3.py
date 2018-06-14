#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (54.97%)
# Total Accepted:    345.2K
# Total Submissions: 619.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
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
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        series = [(root, 1)]
        level = 0
        while len(series) > 0:
        	node = series[0]
        	if node[0] == None:
        		del series[0]
        		continue
        	if node[1] != level:
        		level = node[1]
        	series.append((node[0].left, level + 1))
        	series.append((node[0].right, level + 1))
        	del series[0]
        return level
        
