#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (20.33%)
# Total Accepted:    177.6K
# Total Submissions: 865.6K
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.dfs(s, {})

    def dfs(self, s, records):
        if s in records.keys():
            return records[s]
        if len(s) == 0:
            return 1
        if s[0:1] == "0":
            return 0
        if len(s) == 1:
            return 1
        if int(s[:2]) <= 26:
            records[s] = self.dfs(s[1:], records) + self.dfs(s[2:], records)
        else:
            records[s] = self.dfs(s[1:], records)
        return records[s]

        
