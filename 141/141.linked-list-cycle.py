#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (34.88%)
# Total Accepted:    276.6K
# Total Submissions: 794.4K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, determine if it has a cycle in it.
# 
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
        	return False
        slow_ptr = head
        fast_ptr = head
        while True:
        	try:
        		slow_ptr = slow_ptr.next
        		fast_ptr = fast_ptr.next.next
        	except:
        		return False
        	if slow_ptr == fast_ptr:
        		return True
