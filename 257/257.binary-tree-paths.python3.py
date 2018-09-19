#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (42.99%)
# Total Accepted:    181.3K
# Total Submissions: 421.7K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        self.dfs(root, "", ans)
        return ans
    
    def dfs(self, root, path, ans):
    	if root == None:
    		return
    	if root.left == None and root.right == None:
    		ans.append(path + str(root.val))
    		return
    	if root.left != None:
    		self.dfs(root.left, "{}{}->".format(path, root.val), ans)
    	if root.right != None:
    		self.dfs(root.right, "{}{}->".format(path, root.val), ans)
    	return
