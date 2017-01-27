import copy
class Solution(object):
    def totalNQueens(self, n):
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
        return self.dfs(col_record, record1, record2, [], 0, n, 0)
    def dfs(self, col_record, record1, record2, result, cnt, n, total_result):
    	if cnt == n:
    		return 1
        number = 0
    	for i in range(n):
    		if col_record[i] == True and record1[cnt + n - 1 - i] == True and record2[cnt + i] == True:
    			col_record[i] = False
    			record1[cnt + n - 1 - i] = False
    			record2[cnt + i] = False
    			result.append(i)
    			number = number + self.dfs(col_record, record1, record2, result, cnt + 1, n, total_result)
    			result.pop()
    			record2[cnt + i] = True
    			record1[cnt + n - 1 - i] = True
    			col_record[i] = True
        return number
