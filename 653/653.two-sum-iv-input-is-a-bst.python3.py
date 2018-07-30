#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (50.27%)
# Total Accepted:    49.6K
# Total Submissions: 98.6K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
# 
# Example 1:
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# Output: False
# 
# 
# 
# 
#
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        sorted_array = []
        self.dfs(root, sorted_array)
        left_ptr = 0
        right_ptr = len(sorted_array) - 1
        while left_ptr < right_ptr:
        	if sorted_array[left_ptr] + sorted_array[right_ptr] == k:
        		return True
        	elif sorted_array[left_ptr] + sorted_array[right_ptr] < k:
        		left_ptr += 1
        	else:
        		right_ptr -= 1
        return False

    def dfs(self, root, sorted_array):
    	if root == None:
    		return
    	self.dfs(root.left, sorted_array)
    	sorted_array.append(root.val)
    	self.dfs(root.right, sorted_array)
    	return








        
