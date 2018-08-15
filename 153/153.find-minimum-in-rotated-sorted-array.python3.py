#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (41.21%)
# Total Accepted:    213.3K
# Total Submissions: 515.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = int((left + right) / 2)
        if nums[mid] < nums[left]:
            return self.dfs(nums, left, mid)
        elif nums[mid] > nums[right]:
            return self.dfs(nums, mid + 1, right)
        else:
            return self.dfs(nums, left, mid)
        
