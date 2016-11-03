class Solution
{
public:
	string convert(string s, int numRows)
	{
		string result = s;
		int cnt = 0;
		for (int i = 0; i < numRows; i++)
		{
			int ptr = i;
			bool move = true;
			while(ptr < s.length())
			{
				int temp = ptr;
				if (i == 0)
				{
					result[cnt] = s[ptr];
					cnt++;
					ptr += 2 * (numRows - 1);
				}
				else if (i == numRows - 1)
				{
					result[cnt] = s[ptr];
					cnt++;
					ptr += 2 * (numRows - 1);
				}
				else
				{
					if (move == true)
					{
						result[cnt] = s[ptr];
						cnt++;
						ptr += 2 * (numRows - 1 - i);
						move = false;
					}
					else
					{
						result[cnt] = s[ptr];
						cnt++;
						ptr += 2 * i;
						move = true;	
					}
				}
				if (temp == ptr)
					break;
			}
		}
		return result;
	}
};