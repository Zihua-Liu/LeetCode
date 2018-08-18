#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (25.14%)
# Total Accepted:    123.6K
# Total Submissions: 491.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
import copy
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not self.isValid(s, wordDict):
        	return []

        tmp_result = []
        self.dfs(s, wordDict, [], tmp_result)
        result = []
        for array in tmp_result:
        	if array != []:
        		string = array[0]
        		for i in range(1, len(array)):
        			string += " {}".format(array[i])
        		result.append(string)
        return result

    def isValid(self, s, wordDict):
    	valid = [True]
    	for i in range(1, len(s) + 1):
    		valid.append(False)
    		for j in range(i - 1, -1, -1):
    			if valid[j] and s[j:i] in wordDict:
    				valid[i] = True
    				break
    	return valid[-1]    

    def dfs(self, s, wordDict, record, result):
    	if s == "" and record not in result:
    		result.append(copy.deepcopy(record))
    	for word in wordDict:
    		if s[0:len(word)] == word:
    			record.append(word)
    			self.dfs(s[len(word):], wordDict, record, result)
    			record.pop()
    	return

        
