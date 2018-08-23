#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (43.22%)
# Total Accepted:    192.8K
# Total Submissions: 442.4K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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

class StackElement:
    def __init__(self, node, tag):
        self.node = node
        self.tag = tag

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if root == None:
            return result
        ptr = root

        while stack != [] or ptr != None:
            while ptr != None:
                stack.append(StackElement(ptr, "left"))
                ptr = ptr.left
            ele = stack[-1]
            stack.pop()
            ptr = ele.node
            if ele.tag == "left":
                ele.tag = "right"
                stack.append(ele)
                ptr = ptr.right
            else:
                result.append(ptr.val)
                ptr = None
        return result















        
