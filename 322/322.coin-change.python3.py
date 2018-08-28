#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (27.08%)
# Total Accepted:    113K
# Total Submissions: 416.4K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        record = [None for i in range(0, amount + 1)]
        coins.sort()
        for coin in coins:
            if coin > amount:
                break
            record[coin] = 1
        min_coin = min(coins)
        for i in range(0, amount + 1):
            if i < min_coin:
                continue
            if record[i] != None:
                continue
            ans = float('inf')
            for j in range(len(coins)):
                if i - coins[j] < min_coin:
                    break
                if record[i - coins[j]] != None:
                    ans = min(ans, 1 + record[i - coins[j]])
            if ans != float('inf'):
                record[i] = ans
        if record[amount] != None:
            return record[amount]
        else:
            return -1
sol = Solution()
print(sol.coinChange([259,78,94,130,493,4,168,149], 4769))
        
