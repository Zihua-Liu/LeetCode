class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		records = []
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		for i in range(m + 1):
			records.append([])
			for j in range(n + 1):
				records[i].append(-1)
		return self.dfs(obstacleGrid, records, 0, 0, m - 1, n - 1)
	
	def dfs(self, obstacleGrid, records, x, y, m, n):
		if records[x][y] != -1:
			return records[x][y]
		if obstacleGrid[x][y] == 1:
			return 0
		if x == m and y == n:
			records[x][y] = 1
			return 1
		if x == m:
			records[x][y] = self.dfs(obstacleGrid, records, x, y + 1, m, n)
			return records[x][y]
		if y == n:
			records[x][y] = self.dfs(obstacleGrid, records, x + 1, y, m, n)
			return records[x][y]
		records[x][y] = self.dfs(obstacleGrid, records, x + 1, y, m, n) + self.dfs(obstacleGrid, records, x, y + 1, m, n)
		return records[x][y]
		