#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (28.61%)
# Total Accepted:    87.3K
# Total Submissions: 304.9K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        	return 0
        left_height = 0
        right_height = 0
        left_ptr = root
        right_ptr = root
        while left_ptr != None:
        	left_ptr = left_ptr.left
        	left_height += 1
        while right_ptr != None:
        	right_ptr = right_ptr.right
        	right_height += 1
        if left_height == right_height:
        	return (1 << left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
