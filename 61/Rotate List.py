# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head == None:
            return None
        total_node_cnt = 0
        prev_node = None
        current_node = head
        while current_node != None:
            total_node_cnt += 1
            prev_node = current_node
            current_node = current_node.next          
        last_node = prev_node
        last_node.next = head

        prev_node = head
        current_node = head
        k = k % total_node_cnt
        step_cnt = total_node_cnt - k
        while step_cnt != 0:
            step_cnt -= 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
        return current_node
