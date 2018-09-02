#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.28%)
# Total Accepted:    159.1K
# Total Submissions: 527.4K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# 
# 
# Note: Do not modify the linked list.
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return None
        slow_ptr = head
        fast_ptr = head
        while True:
        	try:
        		slow_ptr = slow_ptr.next
        		fast_ptr = fast_ptr.next.next
        	except:
        		return None
        	if slow_ptr == fast_ptr:
        		break
        fast_ptr = head
        while fast_ptr != slow_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        return fast_ptr
        
