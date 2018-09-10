#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (38.64%)
# Total Accepted:    128.9K
# Total Submissions: 333.1K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# 
#
import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = [0, 1]
        for i in range(2, n + 1):
        	record.append(i)
        	for j in range(1, int(math.sqrt(i)) + 1):
        		record[i] = min(record[i], record[i - j ** 2] + 1)
        return record[n]

        
