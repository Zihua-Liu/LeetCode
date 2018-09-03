#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (29.56%)
# Total Accepted:    127.3K
# Total Submissions: 430.4K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ans = 0
        stack = []
        for tok in tokens:
        	try:
        		stack.append(int(tok))
        	except:
        		num2 = stack[-1]
        		num1 = stack[-2]
        		stack.pop()
        		stack.pop()
        		if tok == "+":
        			stack.append(num1 + num2)
        		elif tok == "-":
        			stack.append(num1 - num2)
        		elif tok == "*":
        			stack.append(num1 * num2)
        		else:
        			if num1 == 0:
        				stack.append(0)
        				continue
        			minus = (num1 * num2) / abs(num1 * num2)
        			stack.append(minus * (abs(num1) // abs(num2)))
        return int(stack[0])

sol = Solution()
sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])        
