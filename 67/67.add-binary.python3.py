#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (34.07%)
# Total Accepted:    197.9K
# Total Submissions: 580.7K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = [0]
        a_list = self.str_to_list(a)
        b_list = self.str_to_list(b)
        for i in range(max(len(a), len(b))):
        	if i < len(a) and i < len(b):
        		result.append(int((result[i] + a_list[i] + b_list[i]) / 2))
        		result[i] = int((result[i] + a_list[i] + b_list[i]) % 2)
        	elif i < len(a):
        		result.append(int((result[i] + a_list[i]) / 2))
        		result[i] = int((result[i] + a_list[i]) % 2)
        	elif i < len(b):
        		result.append(int((result[i] + b_list[i]) / 2))
        		result[i] = int((result[i] + b_list[i]) % 2)
        
        i = len(result) - 1
        while i >= 0 and result[i] == 0:
        	i -= 1
        if i < 0:
        	return '0'
        result_str = ""
        while i >= 0:
        	result_str += str(result[i])
        	i -= 1
        return result_str


    def str_to_list(self, s):
    	result = []
    	for i in range(len(s)):
    		if i == 0:
    			result.append(int(s[-1:]))
    			continue
    		result.append(int(s[-1 - i:-i]))
    	return result

        
