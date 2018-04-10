class Solution
{
public:
	int reverse(int x)
	{
		long long max_int = 0x7fffffff;
		long long min_int = 0xFFFFFFFF80000000;
		if (x >= 0)
		{
			long long sum = 0;
			while(x > 0)
			{
				sum = sum * 10 + (x % 10);
				x = x / 10;
			}
			if (sum > max_int)
				return 0;
			else
				return sum;
		}
		else
		{
			x = 0 - x;
			long long sum = 0;
			while(x > 0)
			{
				sum = sum * 10 + (x % 10);
				x = x / 10;
			}
			if (0 - sum < min_int)
				return 0;
			else
				return 0 - sum;
		}
	}
};
