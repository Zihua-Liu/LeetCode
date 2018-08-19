#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (22.36%)
# Total Accepted:    104.1K
# Total Submissions: 465.4K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodstudentgoodword",
# ⁠ words = ["word","student"]
# Output: []
# 
# 
#
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or words == []:
            return []
        result = []
        total_words_length = len(words) * len(words[0])
        invalid_string = []
        for i in range(0, len(s) - total_words_length + 1):
            if s[i:i + total_words_length] in invalid_string:
                continue
            if self.dfs(s[i:], words):
                result.append(i)
            else:
                invalid_string.append(s[i:i + total_words_length])
        return result

    
    def dfs(self, s, words):
        if words == []:
            return True
        if s == "":
            return False
        invalid_string = []
        for i in range(len(words)):
            word = words[i]
            if word in invalid_string:
                continue
            if s.startswith(word):
                words.pop(i)
                result = self.dfs(s[len(word):], words)
                words.insert(i, word)
                if result:
                    return result
                else:
                    invalid_string.append(word)
        return False       
