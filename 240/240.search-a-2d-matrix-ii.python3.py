#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (39.18%)
# Total Accepted:    124.5K
# Total Submissions: 317.4K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for array in matrix:
            if array == []:
                return False
            if array[0] <= target and array[-1] >= target:
                if self.binarySearch(array, target):
                    return True
                else:
                    continue
        return False

    def binarySearch(self, array, target):
        left = 0
        right = len(array) - 1
        while left < right:
            mid = int((left + right + 1) / 2)
            if array[mid] > target:
                right = mid - 1
            elif array[mid] < target:
                left = mid + 1
            else:
                return True
        if array[left] == target or array[right] == target:
            return True
        return False

        
