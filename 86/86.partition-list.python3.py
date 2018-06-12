#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (33.55%)
# Total Accepted:    126K
# Total Submissions: 371.9K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_head = ListNode(None)
        left_prev = left_head
        right_head = ListNode(None)
        right_prev = right_head
        current_ptr = head
        while current_ptr != None:
        	if current_ptr.val < x:
        		left_prev.next = current_ptr
        		left_prev = current_ptr
        	else:
        		right_prev.next = current_ptr
        		right_prev = current_ptr
        	current_ptr = current_ptr.next
        left_prev.next = right_head.next
        right_prev.next = None
        return left_head.next


