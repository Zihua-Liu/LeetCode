#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (30.71%)
# Total Accepted:    12.1K
# Total Submissions: 39.4K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 109 + 7.
# 
# Example 1:
# 
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
# 
# 
# 
# 
# Note:
# 
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
# 
# 
#
import copy
class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N == 0:
        	return 0
        record = []
        for i_ in range(m):
        	record.append([])
        	for j_ in range(n):
        		record[i_].append(0)
        		if i_ == 0:
        			record[i_][j_] += 1
        		if j_ == 0:
        			record[i_][j_] += 1
        		if i_ == m - 1:
        			record[i_][j_] += 1
        		if j_ == n - 1:
        			record[i_][j_] += 1
        record_init = copy.deepcopy(record)
        for step in range(2, N + 1):
        	tmp_record = copy.deepcopy(record)
        	for i_ in range(m):
        		for j_ in range(n):
        			tmp_record[i_][j_] = record_init[i_][j_]
        			if i_ > 0:
        				tmp_record[i_][j_] += record[i_ - 1][j_]
        			if j_ > 0:
        				tmp_record[i_][j_] += record[i_][j_ - 1]
        			if i_ < m - 1:
        				tmp_record[i_][j_] += record[i_ + 1][j_]
        			if j_ < n - 1:
        				tmp_record[i_][j_] += record[i_][j_ + 1]
        	record = copy.deepcopy(tmp_record)

        return record[i][j] % (10**9 + 7)
        
