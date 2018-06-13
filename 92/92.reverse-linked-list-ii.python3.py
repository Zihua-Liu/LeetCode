#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (31.39%)
# Total Accepted:    142.7K
# Total Submissions: 449.6K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
class Solution:
	def reverseBetween(self, head, m, n):
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
		if m == n:
			return head
		i = 1
		ptr = head
		left_prev_ptr = None
		right_ptr = None
		while ptr != None:
			if i < m:
				if i == m - 1:
					left_prev_ptr = ptr
				ptr = ptr.next
			elif i == m:
				left_ptr = ptr
				prev_ptr = ptr
				ptr = ptr.next
			elif i > m and i < n:
				next_ptr = ptr.next
				ptr.next = prev_ptr
				prev_ptr = ptr
				ptr = next_ptr
			elif i == n:
				next_ptr = ptr.next
				ptr.next = prev_ptr
				prev_ptr = ptr
				right_ptr = ptr
				ptr = next_ptr
			else:
				break
			i += 1
		if left_prev_ptr:
			left_prev_ptr.next = right_ptr
		else:
			head = right_ptr
		left_ptr.next = ptr
		return head



		
