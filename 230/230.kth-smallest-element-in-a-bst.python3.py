#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (47.29%)
# Total Accepted:    165.3K
# Total Submissions: 349.6K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# Output: 1
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
# 
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result, _ = self.dfs(root, k)
        return result

    def dfs(self, root, k):
    	if root == None:
    		return None, 0
    	ans, left_cnt = self.dfs(root.left, k)
    	if ans != None:
    		return ans, None
    	else:
    		if left_cnt + 1 == k:
    			return root.val, None
    		else:
    			ans, right_cnt = self.dfs(root.right, k - left_cnt - 1)
    			if ans != None:
    				return ans, None
    			else:
    				return None, left_cnt + right_cnt + 1

