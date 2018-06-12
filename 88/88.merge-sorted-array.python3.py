#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (32.11%)
# Total Accepted:    244.1K
# Total Submissions: 750.7K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        insert_index = 0
        insert_cnt = 0
        ptr = 0
        while insert_index < m + insert_cnt and ptr < n:
        	ele1 = nums1[insert_index]
        	ele2 = nums2[ptr]
        	if ele2 <= ele1:
        		nums1.insert(insert_index, ele2)
        		insert_index += 1
        		ptr += 1
        		insert_cnt += 1
        	else:
        		insert_index += 1
        for i in range(ptr, n):
        	nums1.insert(insert_index, nums2[i])
        	insert_index += 1
        for i in range(m + n, len(nums1)):
        	nums1.pop()
        
