/*
 * [322] Coin Change
 *
 * https://leetcode.com/problems/coin-change/description/
 *
 * algorithms
 * Medium (27.08%)
 * Total Accepted:    113K
 * Total Submissions: 416.4K
 * Testcase Example:  '[1,2,5]\n11'
 *
 * You are given coins of different denominations and a total amount of money
 * amount. Write a function to compute the fewest number of coins that you need
 * to make up that amount. If that amount of money cannot be made up by any
 * combination of the coins, return -1.
 * 
 * Example 1:
 * 
 * 
 * Input: coins = [1, 2, 5], amount = 11
 * Output: 3 
 * Explanation: 11 = 5 + 5 + 1
 * 
 * Example 2:
 * 
 * 
 * Input: coins = [2], amount = 3
 * Output: -1
 * 
 * 
 * Note:
 * You may assume that you have an infinite number of each kind of coin.
 * 
 */
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0)
        	return 0;
        vector<int> record(amount + 1, 0);
        sort(coins.begin(), coins.end());
        for (auto coin : coins)
        {
        	if (coin > amount)
        		break;
        	record[coin] = 1;
        }
        int min_coin = coins[0];
        for (int i = 0; i <= amount; i++)
        {
        	if (i < min_coin)
        		continue;
        	if (record[i] != 0)
        		continue;
        	int ans = 1 << 30;
        	for (auto coin : coins)
        	{
        		if (i - coin < min_coin)
        			break;
        		if (record[i - coin] != 0)
        			ans = min(ans, 1 + record[i - coin]);
        	}
        	if (ans != 1 << 30)
        		record[i] = ans;
        }
        if (record[amount] != 0)
        	return record[amount];
        else
        	return -1;
    }
};
