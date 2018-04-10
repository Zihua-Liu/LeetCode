class Solution 
{
public:
	string longestPalindrome(string s) 
	{
        		bool record[1000][1000];
        		int result_l = 0, result_r = 0;
        		for (int length = 1; length <= s.length(); length++)
        		{
        			for (int i = 0; i < s.length() - length + 1; i++)
        			{
        				int j = i + length - 1;
        				if (length == 1)
        				{
        					record[i][j] = true;
        					break;
        				}
        				else if (length == 2)
        				{
        					if(s[i] == s[j])
        					{
        						record[i][j] = true;
        						result_l = i;
        						result_r = j;
        					}
        					else
        						record[i][j] = false;
        					break;
        				}
        				else
        				{
        					if (s[i] == s[j] && record[i+1][j-1] == true)
        					{
        						record[i][j] = true;
        						result_l = i;
        						result_r = j;
        					}
        					else
        						record[i][j] = false;
        					break;
        				}
        			}
        		}
        		return s.substr(result_l, result_r - result_l + 1);
	}
};