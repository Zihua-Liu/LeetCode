class Solution {
public:
	int lengthOfLongestSubstring(string s) 
	{
		int *record = new int[26];
		int max_result = 0;
		for (int i = 0; i < s.length(); i++)
		{
			memset(record, 0, 26 * sizeof(int));
			int result = 1;
			record[s[i] - 'a'] = 1;
			for (int j = i + 1; j < s.length(); j++)
			{
				if (record[s[j] - 'a'] == 0)
				{
					result++;
					record[s[j] - 'a'] = 1;
				}
				else
					break;
			}
			if (result > max_result)
				max_result = result;
		}
		return max_result;        
	}
};