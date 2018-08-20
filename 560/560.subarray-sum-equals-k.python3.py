#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (39.85%)
# Total Accepted:    45.6K
# Total Submissions: 114.4K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
#
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_set = {0:1}
        total = 0
        result = 0
        for num in nums:
            total += num
            if total - k in hash_set.keys():
                result += hash_set[total - k]
            if total not in hash_set.keys():
                hash_set[total] = 1
            else:
                hash_set[total] += 1
        return result

