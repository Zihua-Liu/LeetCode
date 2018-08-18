#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (44.23%)
# Total Accepted:    44.2K
# Total Submissions: 99.8K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
# 
# Find the maximum coins you can collect by bursting the balloons wisely.
# 
# Note:
# 
# 
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# Example:
# 
# 
# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
#
import numpy
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        nums.append(1)
        record = []
        for i in range(len(nums)):
        	record.append([])
        	for j in range(len(nums)):
        		record[i].append(0)
        for i in range(1, len(nums) - 1):
        	record[i][i] = nums[i - 1] * nums[i] * nums[i + 1]

        for length in range(1, len(nums) - 1):
        	for i in range(1, len(nums) - 1 - length):
        		j = i + length
        		print((i, j))
        		for k in range(i, j + 1):
        			record[i][j] = max(record[i][j], record[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + record[k + 1][j])

        return record[1][len(nums) - 2]

        
