#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (34.08%)
# Total Accepted:    108.1K
# Total Submissions: 317K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sub_total = []
        if nums != []:
            self.sub_total.append(nums[0])
        for i in range(1, len(nums)):
            self.sub_total.append(nums[i] + self.sub_total[i - 1])
        return
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sub_total[j]
        else:
            return self.sub_total[j] - self.sub_total[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
