#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.35%)
# Total Accepted:    150.9K
# Total Submissions: 389.1K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dic = {}
        for num in nums:
            if num not in num_dic.keys():
                num_dic[num] = 1
            else:
                num_dic[num] += 1
        prev_result = [[]]
        for num in num_dic.keys():
            result = []
            for subset in prev_result:
                for i in range(num_dic[num] + 1):
                    tmp_subset = []
                    for j in range(0, i):
                        tmp_subset.append(num)
                    result.append(tmp_subset + subset)
            prev_result = result
        return result

                

