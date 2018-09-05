#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (34.15%)
# Total Accepted:    173.3K
# Total Submissions: 507.4K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        virtual_head = ListNode(None)
        virtual_head.next = head
        ptr = virtual_head
        while ptr.next != None:
        	if ptr.next.val == val:
        		ptr.next = ptr.next.next
        	else:
        		ptr = ptr.next
        return virtual_head.next


        
