#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (47.83%)
# Total Accepted:    383K
# Total Submissions: 793.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return None
        prev_ptr = head
        ptr = head.next
        while ptr != None:
        	tmp_ptr = ptr
        	next_ptr = ptr.next
        	ptr.next = prev_ptr
        	ptr = next_ptr
        	prev_ptr = tmp_ptr
        head.next = None
        return prev_ptr

        
