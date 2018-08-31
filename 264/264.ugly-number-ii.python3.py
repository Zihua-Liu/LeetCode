#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (34.03%)
# Total Accepted:    82.9K
# Total Submissions: 243.4K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
# 
#
import heapq
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        heapq.heapify(heap)
        lastnum = -1
        i = 0
        while i < n:
            top = heapq.heappop(heap)
            if top == lastnum:
                continue
            heapq.heappush(heap, top * 2)
            heapq.heappush(heap, top * 3)
            heapq.heappush(heap, top * 5)
            lastnum = top
            i += 1
        return top

        
        	
        
