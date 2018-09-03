#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (49.33%)
# Total Accepted:    292K
# Total Submissions: 591.9K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = {}
        for num in nums:
        	if num not in hash_set.keys():
        		hash_set[num] = 1
        	else:
        		hash_set[num] += 1
        nums.sort(key = lambda x: hash_set[x], reverse = True)
        return nums[0]
