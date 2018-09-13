#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (29.71%)
# Total Accepted:    75.7K
# Total Submissions: 254.5K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# Example 1:
# 
# 
# Input: "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
import re
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = []
        i = 0
        while i < len(s):
        	if s[i] in ["+", "-", "(", ")", " "]:
        		list_s.append(s[i])
        		i += 1
        	else:
        		num_str = ""
        		while i < len(s) and s[i] not in ["+", "-", "(", ")", " "]:
        			num_str += s[i]
        			i += 1
        		list_s.append(num_str)
        s = self.convert_to_postfix(list_s)
        stack = []
        ans = 0
        for item in s:
        	if item in ["+", "-"]:
        		num2 = int(stack[-1])
        		num1 = int(stack[-2])
        		stack.pop()
        		stack.pop()
        		if item == "+":
        			stack.append(num1 + num2)
        		else:
        			stack.append(num1 - num2)
        	else:
        		stack.append(item)
        return int(stack[-1])



    def convert_to_postfix(self, s):
    	ans = []
    	stack = []
    	for char in s:
    		if char == " ":
    			continue
    		if char == "(":
    			stack.append(char)
    		elif char == ")":
    			while stack[-1] != "(":
    				ans.append(stack[-1])
    				stack.pop()
    			stack.pop()
    		elif char in ["+", "-"]:
    			while stack != [] and stack[-1] != "(":
    				ans.append(stack[-1])
    				stack.pop()
    			stack.append(char)
    		else:
    			ans.append(char)
    	while stack != []:
    		ans.append(stack[-1])
    		stack.pop()
    	return ans
sol = Solution()
print(sol.calculate("1+1"))

        
