#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (49.13%)
# Total Accepted:    27.7K
# Total Submissions: 56.3K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 231.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# 
#
class Node:
	def __init__(self):
		self.left = None
		self.right = None
		self.val = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = Node()
        for num in nums:
        	ptr = root
        	for i in range(32)[::-1]:
        		if (num >> i) & 1 == 1:
        			if ptr.left == None:
        				ptr.left = Node()
        			ptr = ptr.left
        		else:
        			if ptr.right == None:
        				ptr.right = Node()
        			ptr = ptr.right
        	ptr.val = num
        ans = 0
        for num in nums:
        	ptr = root
        	partner_ptr = root
        	for i in range(32)[::-1]:
        		if (num >> i) & 1 == 1:
        			ptr = ptr.left
        			if partner_ptr.right != None:
        				partner_ptr = partner_ptr.right
        			else:
        				partner_ptr = partner_ptr.left
        		else:
        			ptr = ptr.right
        			if partner_ptr.left != None:
        				partner_ptr = partner_ptr.left
        			else:
        				partner_ptr = partner_ptr.right
        	if ptr.val ^ partner_ptr.val > ans:
        		ans = ptr.val ^ partner_ptr.val
        return ans
        
