#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (28.04%)
# Total Accepted:    129.3K
# Total Submissions: 455.7K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(-1)
        stack = []
        result = 0
        for i in range(len(heights)):
            while stack != [] and heights[i] < heights[stack[-1]]:
                current = stack[-1]
                stack.pop()
                if stack != []:
                    result = max(result, heights[current] * (i - 1 - (stack[-1] + 1) + 1))
                else:
                    result = max(result, heights[current] * (i - 1 - 0 + 1))
                print(result)
            stack.append(i)
        return result
sol = Solution()
sol.largestRectangleArea([2, 0, 2])


        
