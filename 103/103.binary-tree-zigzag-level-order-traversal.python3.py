#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (36.81%)
# Total Accepted:    143.2K
# Total Submissions: 383.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root):
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
        for i in range(0, len(result)):
        	if i % 2 == 1:
        		result[i].reverse()
        return result
        
