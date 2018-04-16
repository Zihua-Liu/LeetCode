class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        records = []
        for i in range(m + 1):
        	records.append([])
        	for j in range(n + 1):
        		records[i].append(-1)
        return self.dfs(records, 1, 1, m, n)
    
    def dfs(self, records, x, y, m, n):
    	if records[x][y] != -1:
    		return records[x][y]

    	if x == m and y == n:
    		records[x][y] = 1
    		return 1
    	if x == m:
    		records[x][y] = self.dfs(records, x, y + 1, m, n)
    		return records[x][y]
    	if y == n:
    		records[x][y] = self.dfs(records, x + 1, y, m, n)
    		return records[x][y]
    	records[x][y] = self.dfs(records, x + 1, y, m, n) + self.dfs(records, x, y + 1, m, n)
    	return records[x][y]