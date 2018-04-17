#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (41.26%)
# Total Accepted:    245.7K
# Total Submissions: 595.4K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        records = []
        for i in range(n + 1):
        	records.append(-1)
        return self.dfs(n, records)

    def dfs(self, n, records):
    	if records[n] != -1:
    		return records[n]
    	if n == 0:
    		records[n] = 1
    		return records[n]
    	if n < 0:
    		return 0
    	records[n] = self.dfs(n - 1, records) + self.dfs(n - 2, records)
    	return records[n]







        
