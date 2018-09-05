#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (35.39%)
# Total Accepted:    154.5K
# Total Submissions: 436.5K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        hash_set = {}
        hash_set_reverse = {}
        for i in range(len(s)):
        	if s[i] not in hash_set.keys():
        		hash_set[s[i]] = t[i]
        	else:
        		if hash_set[s[i]] != t[i]:
        			return False

        	if t[i] not in hash_set_reverse.keys():
        		hash_set_reverse[t[i]] = s[i]
        	else:
        		if hash_set_reverse[t[i]] != s[i]:
        			return False
        return True
        

        
