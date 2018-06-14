#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (42.25%)
# Total Accepted:    169.6K
# Total Submissions: 396.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
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

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        series = [(root, 0)]
        result = []
        level = -1
        while len(series) > 0:
        	node = series[0]
        	if node[0] == None:
        		del series[0]
        		continue
        	if node[1] != level:
        		result.append([])
        		level = node[1]
        	result[level].append(node[0].val)
        	series.append((node[0].left, level + 1))
        	series.append((node[0].right, level + 1))
        	del series[0]
        result.reverse()
        return result
        
