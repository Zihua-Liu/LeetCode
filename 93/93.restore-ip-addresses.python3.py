#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (28.49%)
# Total Accepted:    106.3K
# Total Submissions: 369.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#
class Solution:
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		result = []
		self.dfs(s, "", result, 1)
		return result
	
	
	def dfs(self, s, tmp_result, result, depth):
		if s == "":
			return
		if depth == 4:
			if int(s) == 0 and len(s) == 1:
				result.append(tmp_result + s)
			if 0 < int(s) < 256 and s[0:1] != "0":
				result.append(tmp_result + s)
			return

		if s[0:1] == "0":
			self.dfs(s[1:],tmp_result + "0.", result, depth + 1)
		else:
			self.dfs(s[1:], "{}{}.".format(tmp_result, s[0:1]), result, depth + 1)
			self.dfs(s[2:], "{}{}.".format(tmp_result, s[0:2]), result, depth + 1)
			if int(s[0:3]) <= 255:
				self.dfs(s[3:], "{}{}.".format(tmp_result, s[0:3]), result, depth + 1)

		return