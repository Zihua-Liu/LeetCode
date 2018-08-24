#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (33.82%)
# Total Accepted:    113.4K
# Total Submissions: 335.1K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
# 
#
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_list = list(pattern)
        str_list = str.split(" ")
        if len(pattern_list) != len(str_list):
        	return False
        hash_set = {}
        hash_set_reverse = {}
        for i in range(len(pattern_list)):
        	if pattern_list[i] not in hash_set.keys():
        		hash_set[pattern_list[i]] = str_list[i]
        	else:
        		if hash_set[pattern_list[i]] != str_list[i]:
        			return False
        	if str_list[i] not in hash_set_reverse.keys():
        		hash_set_reverse[str_list[i]] = pattern_list[i]
        	else:
        		if hash_set_reverse[str_list[i]] != pattern_list[i]:
        			return False
        return True
        
