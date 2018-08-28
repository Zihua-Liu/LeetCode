#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (32.74%)
# Total Accepted:    33.1K
# Total Submissions: 101K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
# 
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
# 
# Note:
# Rotation is not allowed.
# 
# Example:
# 
# 
# 
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# 
#
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if envelopes == []:
        	return 0
        envelopes.sort(key = lambda x: x[0])
        record = [1]
        result = 1
        for i in range(1, len(envelopes)):
        	length = 1
        	for j in range(0, i):
        		if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
        			length = max(length, record[j] + 1)
        	record.append(length)
        	result = max(result, length)
        return result
        
