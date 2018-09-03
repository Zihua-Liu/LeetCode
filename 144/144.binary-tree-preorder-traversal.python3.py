#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (48.21%)
# Total Accepted:    256.6K
# Total Submissions: 532.2K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [None]
        ptr = root
        ans = []
        while ptr != None:
        	ans.append(ptr.val)
        	if ptr.right != None:
        		stack.append(ptr.right)
        	if ptr.left != None:
        		ptr = ptr.left
        	else:
        		ptr = stack[-1]
        		stack.pop()
        return ans
        
