#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (23.65%)
# Total Accepted:    290K
# Total Submissions: 1.2M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 0:
        	left = self.findK(nums1, nums2, (len(nums1) + len(nums2)) // 2)
        	right = self.findK(nums1, nums2, (len(nums1) + len(nums2)) // 2 + 1)
        	print(left)
        	print(right)
        	return (left + right) / 2.0
        else:
        	return self.findK(nums1, nums2, (len(nums1) + len(nums2) + 1) // 2)

    def findK(self, nums1, nums2, k):
    	if len(nums1) > len(nums2):
    		return self.findK(nums2, nums1, k)
    	if nums1 == []:
    		return nums2[k - 1]
    	if k == 1:
    		return min(nums1[0], nums2[0])
    	if len(nums1) > k // 2:
    		if nums1[k // 2 - 1] > nums2[k // 2 - 1]:
    			return self.findK(nums1, nums2[k // 2:], k - k // 2)
    		else:
    			return self.findK(nums1[k // 2:], nums2, k - k // 2)
    	else:
    		if nums1[-1] > nums2[len(nums1) - 1]:
    			return self.findK(nums1, nums2[len(nums1):], k - len(nums1))
    		else:
    			return self.findK([], nums2, k - len(nums1))

