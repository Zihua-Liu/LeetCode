class Solution(object):
	def dfs(self, s, n, use_l, use_r):
		if use_l == n and use_r == n:
			return [s]
		if use_l == n:
			return self.dfs(s + ")", n, use_l, use_r + 1)
		if use_l == use_r:
			return self.dfs(s + "(", n, use_l + 1, use_r)
		return self.dfs(s + ")", n, use_l, use_r + 1) + self.dfs(s + "(", n, use_l + 1, use_r)

	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		s = ""
		use_l = 0
		use_r = 0
		return self.dfs(s, n, use_l, use_r)
	
s = Solution()
print(s.generateParenthesis(3))
