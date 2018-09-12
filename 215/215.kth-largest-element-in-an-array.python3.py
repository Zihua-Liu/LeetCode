#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (42.61%)
# Total Accepted:    250.2K
# Total Submissions: 586.7K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
        	return nums[0]
        slot = len(nums) - 1
        l = 0
        r = len(nums) - 2
        divide_num = nums[slot]
        while l <= r:
        	while l <= r and nums[l] > divide_num:
        		l += 1
        	if l <= r:
        		nums[slot] = nums[l]
        		slot = l
        		l += 1
        	while l <= r and nums[r] < divide_num:
        		r -= 1
        	if l <= r:
        		nums[slot] = nums[r]
        		slot = r
        		r -= 1
        nums[slot] = divide_num
        if k - 1 < slot:
        	return self.findKthLargest(nums[0:slot], k)
        elif k - 1 == slot:
        	return nums[slot]
        else:
        	return self.findKthLargest(nums[slot + 1:], k - slot - 1)
        
