#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (33.47%)
# Total Accepted:    109.3K
# Total Submissions: 326.5K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        begin = nums[0]
        current = begin
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == current + 1:
                current += 1
            else:
                if current == begin:
                    ans.append(str(current))
                else:
                    ans.append("{}->{}".format(begin, current))
                begin = nums[i]
                current = nums[i]
        if current == begin:
            ans.append(str(current))
        else:
            ans.append("{}->{}".format(begin, current))
        return ans
        
