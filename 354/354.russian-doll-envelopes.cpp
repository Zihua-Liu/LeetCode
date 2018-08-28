/*
 * [354] Russian Doll Envelopes
 *
 * https://leetcode.com/problems/russian-doll-envelopes/description/
 *
 * algorithms
 * Hard (32.74%)
 * Total Accepted:    33.1K
 * Total Submissions: 101K
 * Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
 *
 * You have a number of envelopes with widths and heights given as a pair of
 * integers (w, h). One envelope can fit into another if and only if both the
 * width and height of one envelope is greater than the width and height of the
 * other envelope.
 * 
 * What is the maximum number of envelopes can you Russian doll? (put one
 * inside other)
 * 
 * Note:
 * Rotation is not allowed.
 * 
 * Example:
 * 
 * 
 * 
 * Input: [[5,4],[6,4],[6,7],[2,3]]
 * Output: 3 
 * Explanation: The maximum number of envelopes you can Russian doll is 3
 * ([2,3] => [5,4] => [6,7]).
 * 
 * 
 * 
 */
class Solution {
public:
    int maxEnvelopes(vector<pair<int, int> >& envelopes) {
        int env_size = envelopes.size();
        if (env_size == 0)
        	return 0;
        sort(envelopes.begin(), envelopes.end());
        vector<int> record(env_size);
        record[0] = 1;
        int result = 1;
        for (int i = 1; i < env_size; i++){
        	int length = 1;
        	for (int j = 0; j < i; j++){
        		if (envelopes[j].first < envelopes[i].first && envelopes[j].second < envelopes[i].second)
        			length = max(length, record[j] + 1);
        	}
        	record[i] = length;
        	result = max(result, length);
        }
        return result;
    }
};
