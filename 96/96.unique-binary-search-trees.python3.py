#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (41.96%)
# Total Accepted:    153.3K
# Total Submissions: 362.1K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
class Solution:
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		record = {}
		return self.dfs(n, record)

	def dfs(self, k, record):
		if k in record.keys():
			return record[k]
		if k in [0, 1]:
			return 1

		cnt = 0
		for i in range(k):
			cnt += self.dfs(i, record) * self.dfs(k - 1 - i, record)
		record[k] = cnt
		return cnt
		
