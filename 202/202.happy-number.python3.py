#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (42.64%)
# Total Accepted:    180.9K
# Total Submissions: 424.2K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
# 
#
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        while True:
        	if n in record:
        		return False
        	record.append(n)
        	str_n = str(n)
        	n = 0
        	for i in range(len(str_n)):
        		n += int(str_n[i]) ** 2
        	if n == 1:
        		return True
        
