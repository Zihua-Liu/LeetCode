#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (27.30%)
# Total Accepted:    118K
# Total Submissions: 429.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
        	return None
        record = []
        ptr = head 
        while ptr != None:
        	record.append(ptr)
        	ptr = ptr.next
        thresold = int((len(record)) / 2)
        for i in range(0, thresold):
        	record[i].next = record[-1 - i]
        	if record[-1 - i] != record[i + 1]:
        		record[-1 - i].next = record[i + 1]
        	else:
        		record[-1 - i].next = None
        if len(record) % 2 == 1:
        	record[thresold].next = None












        
