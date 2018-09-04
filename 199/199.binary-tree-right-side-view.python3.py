#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (44.05%)
# Total Accepted:    122.9K
# Total Submissions: 279K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
        	return []
        queue = [(root, 0)]
        series = []
        while queue != []:
        	head = queue[0]
        	series.append(head)
        	queue.pop(0)
        	if head[0].right != None:
        		queue.append((head[0].right, head[1] + 1))
        	if head[0].left != None:
        		queue.append((head[0].left, head[1] + 1))
        ans = []
        level = 0
        for tup in series:
        	if tup[1] == level:
        		ans.append(tup[0].val)
        		level += 1
        	else:
        		continue
        return ans

        
