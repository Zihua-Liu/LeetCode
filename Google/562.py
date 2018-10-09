class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        h_record = [[-1] * len(M[0]) for i in range(len(M))]
        v_record = [[-1] * len(M[0]) for i in range(len(M))]
        d_record = [[-1] * len(M[0]) for i in range(len(M))]
        ad_record = [[-1] * len(M[0]) for i in range(len(M))]

        ans = 0
        for i in range(len(M)):
        	for j in range(len(M[0])):
        		ans = max(ans, self.dfs_h(i, j, M, h_record), self.dfs_v(i, j, M, v_record), self.dfs_d(i, j, M, d_record), self.dfs_ad(i, j, M, ad_record))
		return ans   

    def dfs_h(self, i, j, M, h_record):
    	if j > len(M[0]) - 1:
    		return 0
    	if h_record[i][j] != -1:
    		return h_record[i][j]
    	if M[i][j] == 0:
    		h_record[i][j] = 0
    		return 0
    	h_record[i][j] = 1 + self.dfs_h(i, j + 1, M, h_record)
    	return h_record[i][j]

    def dfs_v(self, i, j, M, v_record):
    	if i > len(M) - 1:
    		return 0
    	if v_record[i][j] != -1:
    		return v_record[i][j]
    	if M[i][j] == 0:
    		v_record[i][j] = 0
    		return 0
    	v_record[i][j] = 1 + self.dfs_v(i + 1, j, M, v_record)
    	return v_record[i][j]

    def dfs_d(self, i, j, M, h_record):
    	if i > len(M) - 1 or j > len(M[0]) - 1:
    		return 0
    	if d_record[i][j] != -1:
    		return d_record[i][j]
    	if M[i][j] == 0:
    		d_record[i][j] = 0
    		return 0
    	d_record[i][j] = 1 + self.dfs_d(i + 1, j + 1, M, d_record)
    	return d_record[i][j]

    def dfs_ad(self, i, j, M, h_record):
    	if j < 0 or i > len(M) - 1:
    		return 0
    	if ad_record[i][j] != -1:
    		return ad_record[i][j]
    	if M[i][j] == 0:
    		ad_record[i][j] = 0
    		return 0
    	ad_record[i][j] = 1 + self.dfs_ad(i + 1, j - 1, M, ad_record)
    	return ad_record[i][j]