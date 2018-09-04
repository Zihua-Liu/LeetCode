#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (29.28%)
# Total Accepted:    147.7K
# Total Submissions: 504.5K
# Testcase Example:  '    43261596 (00000010100101000001111010011100)'
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# Example:
# 
# 
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as
# 00000010100101000001111010011100, 
# return 964176192 represented in binary as 00111001011110000010100101000000.
# 
# 
# Follow up:
# If this function is called many times, how would you optimize it?
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	ans = []
    	while True:
    		ans.append(n % 2)
    		n = n // 2
    		if n == 0:
    			break
    	for i in range(len(ans), 32):
    		ans.append(0)
    	result = 0
    	print(ans)
    	for num in ans:
    		result += num
    		result *= 2
    	result //= 2
    	print(result)
    	return result
sol = Solution()
sol.reverseBits(43261596)
