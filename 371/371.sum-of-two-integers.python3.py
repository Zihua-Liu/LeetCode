#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.85%)
# Total Accepted:    109.6K
# Total Submissions: 215.6K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        carry = 0
        ans = 0
        for i in range(0, 32):
        	num1 = (a >> i) & 1
        	num2 = (b >> i) & 1
        	result = num1 ^ num2 ^ carry
        	carry = (num1 & num2) | (num1 & carry) | (num2 & carry)
        	ans += (result << i)
        if ans > 0x7fffffff:
        	ans =  - (ans ^ 0xffffffff) - 1
        return ans
sol = Solution()
print(sol.getSum(-1, -1))
        
