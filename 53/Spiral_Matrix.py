class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
        	return []
        i = 0
        j = 0
        cnt = 0
        result = []
        up = 1
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while True:
        	while j <= right and cnt < len(matrix) * len(matrix[0]):
        		result.append(matrix[i][j])
        		j = j + 1
        		cnt = cnt + 1
        	if cnt == len(matrix) * len(matrix[0]):
        		break
        	else:
        		j = j - 1
        		i = i + 1

        	while i <= down and cnt < len(matrix) * len(matrix[0]):
        		result.append(matrix[i][j])
        		i = i + 1
        		cnt = cnt + 1
        	if cnt == len(matrix) * len(matrix[0]):
        		break
        	else:
        		i = i - 1
        		j = j - 1

        	while j >= left and cnt < len(matrix) * len(matrix[0]):
        		result.append(matrix[i][j])
        		j = j - 1
        		cnt = cnt + 1
        	if cnt == len(matrix) * len(matrix[0]):
        		break
        	else:
        		j = j + 1
        		i = i - 1

        	while i >= up and cnt < len(matrix) * len(matrix[0]):
        		result.append(matrix[i][j])
        		i = i - 1
        		cnt = cnt + 1
        	if cnt == len(matrix) * len(matrix[0]):
        		break
        	else:
        		i = i + 1
        		j = j + 1

        	up = up + 1
        	down = down - 1
        	left = left + 1
        	right = right - 1
        return result