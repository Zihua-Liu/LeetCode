#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (42.69%)
# Total Accepted:    71.3K
# Total Submissions: 167.1K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
# 
#
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
        	return 0
        buy = [-prices[0]]
        sell = [0]
        max_buy = buy[0]
        max_sell = sell[0]
        for i in range(1, len(prices)):
        	sell.append(max_buy + prices[i])
        	profit = max(0, max_sell)
        	buy.append(profit - prices[i])
        	max_sell = max(max_sell, sell[i - 1])
        	max_buy = max(max_buy, buy[i])
        max_sell = max(max_sell, sell[-1])
        return max(0, max_sell)
sol = Solution()
print(sol.maxProfit([1, 2, 3, 0, 2]))
