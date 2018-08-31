#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (45.40%)
# Total Accepted:    33.1K
# Total Submissions: 72.8K
# Testcase Example:  '[1,5,2]'
#
# Given an array of scores that are non-negative integers. Player 1 picks one
# of the numbers from either end of the array followed by the player 2 and then
# player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have
# been chosen. The player with the maximum score wins. 
# 
# Given an array of scores, predict whether player 1 is the winner. You can
# assume each player plays to maximize his score. 
# 
# Example 1:
# 
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2
# (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
# then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 +
# 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you
# need to return False.
# 
# 
# 
# Example 2:
# 
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose
# 233.Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
# 
# 
# 
# Note:
# 
# 1 
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
# 
# 
#
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 1:
        	player_A_last_pick = True
        else:
        	player_A_last_pick= False
        f = []
        for i in range(0, len(nums)):
        	f.append([])
        	for j in range(0, len(nums)):
        		f[i].append(0)
        		if i == j and player_A_last_pick:
        			f[i][j] = nums[i]
        playA_turn = player_A_last_pick
        for length in range(2, len(nums) + 1):
        	playA_turn = not playA_turn
        	for i in range(0, len(nums) - length + 1):
        		j = i + length - 1
        		if playA_turn:
        			f[i][j] = max(nums[i] + f[i + 1][j], nums[j] + f[i][j - 1])
        		else:
        			f[i][j] = min(f[i + 1][j], f[i][j - 1])
        return 2 * f[0][len(nums) - 1] >= sum(nums)
        
