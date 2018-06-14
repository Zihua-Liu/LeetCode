#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (35.78%)
# Total Accepted:    135.1K
# Total Submissions: 372.7K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		if head == None:
			return None
		if head.next == None:
			return TreeNode(head.val)
		cnt = 0
		ptr = head
		while ptr != None:
			cnt += 1
			ptr = ptr.next
		root_index = int(cnt / 2)

		i = 0
		ptr = head
		ptr_prev = None
		while i != root_index:
			ptr_prev = ptr
			i += 1
			ptr = ptr.next
		left_head = head
		right_head = ptr.next
		ptr.next = None
		if ptr_prev:
			ptr_prev.next = None

		root = TreeNode(ptr.val)
		root.left = self.sortedListToBST(left_head)
		root.right = self.sortedListToBST(right_head)
		return root
		
