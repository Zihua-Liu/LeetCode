#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (52.94%)
# Total Accepted:    27.7K
# Total Submissions: 52.4K
# Testcase Example:  '2'
#
# 
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1 
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# 
# 
# 
# 
# Now given N, how many beautiful arrangements can you construct?
# 
# 
# Example 1:
# 
# Input: 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# 
# 
# 
# Note:
# 
# N is a positive integer and will not exceed 15.
# 
# 
#
class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        array = range(1, N + 1)
        return self.dfs(array, 1, N, [])

    def dfs(self, array, i, N, record):
    	if i > N:
    		return 1
    	ans = 0
    	for num in array:
    		if num in record:
    			continue
    		if num % i == 0 or i % num == 0:
    			record.append(num)
    			ans += self.dfs(array, i + 1, N, record)
    			record.pop()
    	return ans

        
