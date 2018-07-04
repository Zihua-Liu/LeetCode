#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (20.10%)
# Total Accepted:    106.8K
# Total Submissions: 531.1K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution:
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		for i in range(len(board)):
			for j in range(len(board[0])):
				self.expand(board, i, j)
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == "-":
					board[i][j] = "O"

	
	def expand(self, board, i, j):
		x = len(board) - 1
		y = len(board[0]) - 1
		if board[i][j] in ["X", "-"]:
			return
		queue = [(i, j)]
		board[i][j] = "?"
		series = []
		while len(queue) > 0:
			item = queue.pop(0)
			series.append(item)
			if item[0] - 1 >= 0 and board[item[0] - 1][item[1]] == "O":
				board[item[0] - 1][item[1]] = "?"
				queue.append((item[0] - 1, item[1]))
			if item[0] + 1 <= x and board[item[0] + 1][item[1]] == "O":
				board[item[0] + 1][item[1]] = "?"
				queue.append((item[0] + 1, item[1]))
			if item[1] - 1 >= 0 and board[item[0]][item[1] - 1] == "O":
				board[item[0]][item[1] - 1] = "?"
				queue.append((item[0], item[1] - 1))
			if item[1] + 1 <= y and board[item[0]][item[1] + 1] == "O":
				board[item[0]][item[1] + 1] = "?"
				queue.append((item[0], item[1] + 1))
		surrounded = True
		for item in series:
			if item[0] == 0 or item[0] == x or item[1] == 0 or item[1] == y:
				surrounded = False
		print(surrounded)
		for item in series:
			if surrounded:
				board[item[0]][item[1]] = "X"
			else:
				board[item[0]][item[1]] = "-"
		
