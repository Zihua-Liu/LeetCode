class Solution
{
public:
	int romanToInt(string s)
	{
		char prev = ' ', cur = ' ';
		int result = 0;
		for (int i = s.length() - 1; i >= 0; i--)
		{
			cur = s[i];
			switch (cur)
			{
				case 'M':
					result += 1000;
					prev = s[i];
					break;
				case 'D':
					result += 500;
					prev = s[i];
					break;
				case 'C':
					if (prev == 'D' || prev == 'M')
					{
						result -= 100;
					}
					else
					{
						result += 100;
						prev = s[i];
					}
					break;
				case 'L':
					result += 50;
					prev = s[i];
					break;
				case 'X':
					if (prev == 'L' || prev = 'C')
					{
						result -= 10;
					}
					else
					{
						result += 10;
						prev = s[i];
					}
					break;
				case 'V':
					result += 5;
					prev = s[i];
					break;
				case 'I':
					if (prev == 'V' || prev = 'X')
					{
						result -= 1;
					}
					else
					{
						result += 1;
						prev = s[i];
					}
					break;
			}
		}
		return result;
	}
};
