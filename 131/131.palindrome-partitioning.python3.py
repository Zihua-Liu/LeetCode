#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (36.94%)
# Total Accepted:    130.3K
# Total Submissions: 352.6K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
import copy
class Solution:    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(s, [], result)
        return result

    def dfs(self, s, record, result):
        if s == "":
            if record not in result:
                result.append(copy.copy(record))
        for i in range(len(s)):
            if self.isPalindrome(s[0:i + 1]):
                record.append(s[0:i + 1])
                self.dfs(s[i + 1:], record, result)
                record.pop()
        return

    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        
