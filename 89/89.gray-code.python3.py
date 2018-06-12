#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (42.46%)
# Total Accepted:    109.2K
# Total Submissions: 255.4K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# 
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 
# 
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# 
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# 
# For example, [0,2,3,1] is also a valid gray code sequence according to the
# above definition.
# 
# For now, the judge is able to judge based on one instance of gray code
# sequence. Sorry about that.
# 
#
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return self.dfs(n)

    def dfs(self, n):
    	if n == 0:
    		return [0]
    	tmp_result = self.dfs(n - 1)
    	result = []
    	for i in range(len(tmp_result)):
    		if i % 2 == 0:
    			result.append(tmp_result[i] * 2)
    			result.append(tmp_result[i] * 2 + 1)
    		else:
    			result.append(tmp_result[i] * 2 + 1)
    			result.append(tmp_result[i] * 2)
    	return result

        
