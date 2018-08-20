#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (31.28%)
# Total Accepted:    145K
# Total Submissions: 463.1K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.divideMerge(head)

    def divideMerge(self, head):
    	if head == None:
    		return head
    	if head.next == None:
    		return head

    	cnt = 0
    	ptr = head
    	while ptr != None:
    		cnt += 1
    		ptr = ptr.next
    	ptr = head
    	for i in range(cnt // 2 - 1):
    		ptr = ptr.next
    	head2 = ptr.next
    	ptr.next = None
    	head1 = head
    	head1 = self.divideMerge(head1)
    	head2 = self.divideMerge(head2)
    	return self.mergeSort(head1, head2)

    def mergeSort(self, head1, head2):
    	if head1.val > head2.val:
    		return self.mergeSort(head2, head1)
    	ptr1 = head1
    	ptr2 = head2
    	while ptr2 != None:
    		while ptr1.next != None and ptr2.val > ptr1.next.val:
    			ptr1 = ptr1.next
    		if ptr1.next == None:
    			ptr1.next = ptr2
    			return head1
    		else:
    			ptr1_next = ptr1.next
    			ptr2_next = ptr2.next
    			ptr1.next = ptr2
    			ptr2.next = ptr1_next
    			ptr1 = ptr1.next
    			ptr2 = ptr2_next
    	return head1
        
