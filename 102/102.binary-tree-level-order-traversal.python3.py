#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (42.66%)
# Total Accepted:    249.3K
# Total Submissions: 575.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
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
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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
    def levelOrder(self, root):
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
        return result

        
