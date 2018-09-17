#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (34.19%)
# Total Accepted:    189.8K
# Total Submissions: 555.1K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
        	return True
        cnt = 0
        ptr = head
        while ptr != None:
        	cnt += 1
        	ptr = ptr.next
        ptr = head
        for i in range((cnt + 1) // 2):
        	ptr = ptr.next
        if ptr == None:
        	return True
        ptr_next = ptr.next
        while ptr_next != None:
        	ptr_next_next = ptr_next.next
        	ptr_next.next = ptr
        	ptr = ptr_next
        	ptr_next = ptr_next_next
        right = ptr
        left = head
        for i in range(cnt // 2):
        	if left.val != right.val:
        		return False
        	left = left.next
        	right = right.next
        return True


        
