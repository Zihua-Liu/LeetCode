#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.73%)
# Total Accepted:    172.1K
# Total Submissions: 669.1K
# Testcase Example:  '{}'
#
# 
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# 
# 
# Return a deep copy of the list.
# 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
        	return None
        result_head = RandomListNode(head.label)
        ptr = head
        result_ptr = result_head
        hash_set = {}
        while ptr != None:
        	if ptr.next != None:
        		if ptr.next not in hash_set.keys():
        			hash_set[ptr.next] = RandomListNode(ptr.next.label)
    			result_ptr.next = hash_set[ptr.next]
    		if ptr.random != None:
    			if ptr.random not in hash_set.keys():
    				hash_set[ptr.random] = RandomListNode(ptr.random.label)
    			result_ptr.random = hash_set[ptr.random]
    		ptr = ptr.next
    		result_ptr = result_ptr.next
    	return result_head


