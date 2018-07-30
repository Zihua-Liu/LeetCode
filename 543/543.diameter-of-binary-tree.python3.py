#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (45.06%)
# Total Accepted:    71.7K
# Total Submissions: 158.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_value = -(1 << 29)
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.dfs(root)
        return self.max_value
    def dfs(self, root):
        if root == None:
            return -(1 << 29)
        left_val = self.dfs(root.left)
        right_val = self.dfs(root.right)
        current_val = max(0, 1 + left_val, 1 + right_val, 2 + left_val + right_val)
        if current_val > self.max_value:
            self.max_value = current_val
        return max(0, 1 + left_val, 1 + right_val) 
        
