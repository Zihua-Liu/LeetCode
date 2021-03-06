#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.76%)
# Total Accepted:    210.2K
# Total Submissions: 683.5K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists: 
# 
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗            
# B:     b1 → b2 → b3
# 
# begin to intersect at node c1.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns. 
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
# 
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
        	return None
        ptrA = headA
        ptrB = headB
        lenA = 1
        lenB = 1
        while ptrA.next != None:
        	ptrA = ptrA.next
        	lenA += 1
        while ptrB.next != None:
        	ptrB = ptrB.next
        	lenB += 1
        if ptrA != ptrB:
        	return None
    	ptrA = headA
        ptrB = headB
        if lenA > lenB:
        	for i in range(0, lenA - lenB):
        		ptrA = ptrA.next
        else:
        	for i in range(0, lenB - lenA):
        		ptrB = ptrB.next
        while ptrA != ptrB:
        	ptrA = ptrA.next
        	ptrB = ptrB.next
        return ptrA

        
