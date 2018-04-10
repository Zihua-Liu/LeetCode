class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(int(len(matrix) / 2)):
        	p1 = i
        	p2 = len(matrix) - 1 - i
        	p3 = len(matrix) - 1 - i
        	p4 = i
        	for j in range(i, len(matrix) - i - 1):
        		matrix[p1][j], matrix[j][p2] = matrix[j][p2], matrix[p1][j]
        	for j in range(i + 1, len(matrix) - i):
        		matrix[p3][j], matrix[j][p4] = matrix[j][p4], matrix[p3][j]
        	for j in range(i, len(matrix) - i - 1):
        		matrix[p1][j], matrix[p3][len(matrix) - 1 - j] = matrix[p3][len(matrix) - 1 - j], matrix[p1][j]