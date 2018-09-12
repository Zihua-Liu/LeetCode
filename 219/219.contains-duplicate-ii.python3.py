#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (33.52%)
# Total Accepted:    160.4K
# Total Submissions: 478.3K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
#
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_set = {}
        for i in range(len(nums)):
        	if nums[i] not in hash_set:
        		hash_set[nums[i]] = [i]
        	else:
        		hash_set[nums[i]].append(i)
        		if hash_set[nums[i]][-1] - hash_set[nums[i]][-2] <= k:
        			return True
        return False
