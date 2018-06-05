#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (29.97%)
# Total Accepted:    137.6K
# Total Submissions: 455.1K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        fake_head = ListNode(None)
        fake_head.next = None
        list_ptr = fake_head
        prev_ptr = head
        ptr = head.next
        current_value = head.val
        dup_cnt = 0
        while ptr != None:
            if ptr.val == current_value:
                dup_cnt += 1
            else:
                current_value = ptr.val
                if dup_cnt == 0:
                    list_ptr.next = prev_ptr
                    list_ptr = list_ptr.next
                dup_cnt = 0
            prev_ptr = ptr
            ptr = ptr.next
        if dup_cnt == 0:
            list_ptr.next = prev_ptr
        else:
            list_ptr.next = None
        return fake_head.next




        
