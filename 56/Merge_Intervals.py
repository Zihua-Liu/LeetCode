# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(self.comp)
        for i in range(len(intervals) - 1):
        	if intervals[i].end >= intervals[i + 1].start:
        		intervals[i + 1].start = -1
        		intervals[i].end = max(intervals[i].end, intervals[i+1].end)
        		intervals[i+1].end = -1
        		intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
        result = []
        for ele in intervals:
        	if not (ele.start == -1 and ele.end == -1):
        		result.append(ele)
        return result
    def comp(self, x, y):
    	if x.start > y.start:
    		return 1
    	elif x.start < y.start:
    		return -1
    	else:
    		return 0