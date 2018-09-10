/*
 * [279] Perfect Squares
 *
 * https://leetcode.com/problems/perfect-squares/description/
 *
 * algorithms
 * Medium (38.64%)
 * Total Accepted:    128.9K
 * Total Submissions: 333.1K
 * Testcase Example:  '12'
 *
 * Given a positive integer n, find the least number of perfect square numbers
 * (for example, 1, 4, 9, 16, ...) which sum to n.
 * 
 * Example 1:
 * 
 * 
 * Input: n = 12
 * Output: 3 
 * Explanation: 12 = 4 + 4 + 4.
 * 
 * Example 2:
 * 
 * 
 * Input: n = 13
 * Output: 2
 * Explanation: 13 = 4 + 9.
 * 
 */
class Solution {
public:
    int numSquares(int n) {
    	vector<int> record(n + 1, n);
    	record[0] = 0;
    	for (int i = 1; i <= n; i++)
    	{
    		for (int j = 1; j * j <= i; j++)
    			record[i] = min(record[i], record[i - j * j] + 1);
    	}
    	return record[n];
        
    }
};
