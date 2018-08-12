#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (30.78%)
# Total Accepted:    112.3K
# Total Submissions: 365K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
        	return 0
        A = [0]
        min_price = prices[0]
        for i in range(1, len(prices)):
        	A.append(max(A[i - 1], prices[i] - min_price))
        	if prices[i] < min_price:
        		min_price = prices[i]

        B = [0]
        max_price = prices[-1]
        i = len(prices) - 2
        while i >= 0:
        	B.insert(0, max(B[0], max_price - prices[i]))
        	if prices[i] > max_price:
        		max_price = prices[i]
        	i -= 1
        profit = 0
        for i in range(0, len(prices)):
        	if A[i] > profit:
        		profit = A[i]
        for i in range(0, len(prices) - 1):
        	if A[i] > profit:
        		profit = A[i]
        	if A[i] + B[i + 1] > profit:
        		profit = A[i] + B[i + 1]
        return profit

















