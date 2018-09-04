#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (24.15%)
# Total Accepted:    103.6K
# Total Submissions: 428.8K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
import functools
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(str1, str2):
        	if str1 == str2:
        		return 0
        	if str1.startswith(str2):
        		return compare(str1[len(str2):], str2)
        	if str2.startswith(str1):
        		return compare(str1, str2[len(str1):])
        	if str1 < str2:
        		return -1
        	else:
        		return 1 
        str_nums = [str(num) for num in nums]
        str_nums.sort(key = functools.cmp_to_key(compare), reverse = True)
        ans = "".join(str_nums)  
        if int(ans) == 0:
        	return "0"
        else:
        	return ans   
