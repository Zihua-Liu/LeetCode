class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.record = [[0] * len(matrix[0]) for i in range(len(matrix))]
        self.update_record = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.record[i][j] += matrix[i][j]
                if i > 0:
                    self.record[i][j] += self.record[i - 1][j]
                if j > 0:
                    self.record[i][j] += self.record[i][j - 1]
                if i > 0 and j > 0:
                    self.record[i][j] -= self.record[i - 1][j - 1]
        return
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.update_record[(row, col)] = val



        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = self.record[row2][col2]
        if row1 > 0:
            ans -= self.record[row1 - 1][col2]
        if col1 > 0:
            ans -= self.record[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            ans += self.record[row1 - 1][col1 - 1]
        for row, col in self.update_record.keys():
            if row1 <= row <= row2 and col1 <= col <= col2:
                ans += self.update_record[(row, col)]
                ans -= self.matrix[row][col]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)