# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return None
        if head.next == None:
        	return head
        if head.next.next == None:
        	result_head = head.next
        	result_head.next = head
        	head.next = None
        	return result_head
        if head.next.next.next == None:
        	result_head = head.next
        	head.next = result_head.next
        	result_head.next = head
        	return result_head
        pos_1 = head
        pos_2 = pos_1.next
        pos_3 = pos_2.next
        pos_4 = pos_3.next
        result_head = pos_2
        while True:
        	pos_1.next = pos_4
        	pos_2.next = pos_1
        	pos_1 = pos_3
        	pos_2 = pos_4
        	pos_3 = pos_4.next
        	if pos_3 == None:
        		break
        	pos_4 = pos_3.next
        	if pos_4 == None:
        		break
        
        if pos_3 == None:
        	pos_2.next = pos_1
        	pos_1.next = None
        	return result_head
        if pos_4 == None:
        	pos_1.next = pos_3
        	pos_2.next = pos_1
        	return result_head

