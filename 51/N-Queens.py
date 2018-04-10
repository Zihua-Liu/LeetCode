import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col_record = []
        record1 = []
        record2 = []
        for i in range(n):
        	col_record.append(True)
        	record1.append(True)
        	record1.append(True)
        	record2.append(True)
        	record2.append(True)
        total_result = []
        self.dfs(col_record, record1, record2, [], 0, n, total_result)
        return total_result
    def dfs(self, col_record, record1, record2, result, cnt, n, total_result):
    	if cnt == n:
    		return_result = []
    		for i in range(n):
    			tmp = ""
    			for j in range(n):
    				if result[i] != j:
    					tmp = tmp + '.'
    				else:
    					tmp = tmp + 'Q'
    			return_result.append(tmp)
    		total_result.append(copy.deepcopy(return_result))
    	for i in range(n):
    		if col_record[i] == True and record1[cnt + n - 1 - i] == True and record2[cnt + i] == True:
    			col_record[i] = False
    			record1[cnt + n - 1 - i] = False
    			record2[cnt + i] = False
    			result.append(i)
    			self.dfs(col_record, record1, record2, result, cnt + 1, n, total_result)
    			result.pop()
    			record2[cnt + i] = True
    			record1[cnt + n - 1 - i] = True
    			col_record[i] = True
