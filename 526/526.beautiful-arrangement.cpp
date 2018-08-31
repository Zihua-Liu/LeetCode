/*
 * [526] Beautiful Arrangement
 *
 * https://leetcode.com/problems/beautiful-arrangement/description/
 *
 * algorithms
 * Medium (52.94%)
 * Total Accepted:    27.7K
 * Total Submissions: 52.4K
 * Testcase Example:  '2'
 *
 * 
 * Suppose you have N integers from 1 to N. We define a beautiful arrangement
 * as an array that is constructed by these N numbers successfully if one of
 * the following is true for the ith position (1 
 * The number at the ith position is divisible by i.
 * i is divisible by the number at the ith position.
 * 
 * 
 * 
 * 
 * Now given N, how many beautiful arrangements can you construct?
 * 
 * 
 * Example 1:
 * 
 * Input: 2
 * Output: 2
 * Explanation: 
 * The first beautiful arrangement is [1, 2]:
 * Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
 * Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
 * The second beautiful arrangement is [2, 1]:
 * Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
 * Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 * 
 * 
 * 
 * Note:
 * 
 * N is a positive integer and will not exceed 15.
 * 
 * 
 */
class Solution {
public:
    int countArrangement(int N) {
        vector<int> array(N);
        for (int i = 0; i < N; i++)
        	array[i] = i + 1;
        vector<bool> record(N + 1, false);
        return dfs(array, 1, N, record);
    }

    int dfs(vector<int> &array, int i, int N, vector<bool> &record)
    {
    	if (i > N)
    		return 1;
    	int ans = 0;
    	for (auto num : array)
    	{
    		if (record[num] == true)
    			continue;
    		if (num % i == 0 || i % num == 0)
    		{
    			record[num] = true;
    			ans += dfs(array, i + 1, N, record);
    			record[num] = false;
    		}
    	}
    	return ans;
    }
};





















