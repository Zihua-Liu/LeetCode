#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.22%)
# Total Accepted:    99.1K
# Total Submissions: 651.3K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
# 
#
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 2:
        	return len(points)
        ans = 1
        for i in range(len(points) - 1):
        	hash_set = {}
        	dup = 0
        	for j in range(i + 1, len(points)):
        		point1 = points[i]
        		point2 = points[j]
        		if point1.x == point2.x and point1.y == point2.y:
        			dup += 1
        			continue
        		slope = (point2.y - point1.y) / (point2.x - point1.x) if point1.x != point2.x else None
        		if slope not in hash_set.keys():
        			hash_set[slope] = [i, j]
        		else:
        			if i not in hash_set[slope]:
        				hash_set[slope].append(i)
        			if j not in hash_set[slope]:
        				hash_set[slope].append(j)
        	cnt_list = [len(arr) for arr in hash_set.values()]
        	if cnt_list == []:
        		ans = max(ans, dup + 1)
        	else:
        		ans = max(ans, max(cnt_list) + dup)
        return ans
        
