#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (30.77%)
# Total Accepted:    73.3K
# Total Submissions: 238.1K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        postfix_s = self.convertToPostfixExpression(s)
        print(postfix_s)
        stack = []
        for i in range(len(postfix_s)):
            try:
                stack.append(int(postfix_s[i]))
            except:
                num2 = stack[-1]
                num1 = stack[-2]
                stack.pop()
                stack.pop()
                if postfix_s[i] == "+":
                    stack.append(int(num1) + int(num2))
                elif postfix_s[i] == "-":
                    stack.append(int(num1) - int(num2))
                elif postfix_s[i] == "*":
                    stack.append(int(num1) * int(num2))
                else:
                    stack.append(int(num1) // int(num2))
        return stack[0]

    def convertToPostfixExpression(self, s):
        result = []
        stack = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            try:
                int(s[i])
                start = i
                while i < len(s) and s[i] not in [" ", "+", "-", "*", "/"]:
                    i += 1
                result.append(s[start:i])
            except:
                if s[i] in ["+", "-"]:
                    while stack != []:
                        result.append(stack[-1])
                        stack.pop()
                else:
                    while stack != [] and stack[-1] not in ["+", "-"]:
                        result.append(stack[-1])
                        stack.pop()
                stack.append(s[i])
                i += 1
        while stack != []:
            result.append(stack[-1])
            stack.pop()
        return result
sol = Solution()
print(sol.calculate("1*2-3/4+5*6-7*8+9/10"))

        
