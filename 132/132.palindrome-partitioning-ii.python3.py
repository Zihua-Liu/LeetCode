#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (25.53%)
# Total Accepted:    87.4K
# Total Submissions: 342.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        isPalindrome = []
        for i in range(len(s)):
        	isPalindrome.append([])
        	for j in range(len(s)):
        		isPalindrome[i].append(False)
        		if i == j:
        			isPalindrome[i][j] = True

        for length in range(2, len(s) + 1):
        	for i in range(0, len(s) - length + 1):
        		j = i + length - 1
        		if length == 2:
        			if s[i] == s[j]:
        				isPalindrome[i][j] = True
        		else:
        			if isPalindrome[i + 1][j - 1] and s[i] == s[j]:
        				isPalindrome[i][j] = True

        f = [0]
        for i in range(1, len(s) + 1):
        	f.append(1 << 29)
        	for j in range(0, i):
        		if isPalindrome[j][i - 1]:
        			f[i] = min(f[i], f[j] + 1)
        return f[len(s)] - 1



sol = Solution()
print(sol.minCut("aab"))
        
