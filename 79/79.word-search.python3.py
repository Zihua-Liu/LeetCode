#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (28.13%)
# Total Accepted:    181.7K
# Total Submissions: 641.6K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(0, len(board)):
        	for j in range(0, len(board[0])):
        		if self.dfs(board, word, i, j, []):
        			return True
        return False

    def dfs(self, board, word, i, j, record):
    	if (i, j) in record:
    		return False 
    	if i < 0 or i >= len(board):
    		return False
    	if j < 0 or j >= len(board[0]):
    		return False
    	if word[0] != board[i][j]:
    		return False
    	if len(word) == 1 and word[0] == board[i][j]:
    		return True 
    	record.append((i, j))
    	result = (self.dfs(board, word[1:], i + 1, j, record) 
    		or self.dfs(board, word[1:], i - 1, j, record)
    		or self.dfs(board, word[1:], i, j + 1, record)
    		or self.dfs(board, word[1:], i, j - 1, record))
    	record.pop()
    	return result
        
