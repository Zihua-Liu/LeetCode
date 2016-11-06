class Solution
{
public:
	int myAtoi(string str)
	{
		long long sum = 0;
		int i = 0;
		while(i < str.length() && str[i] == ' ')
			i++;
		if (!((str[i] >= '0' && str[i]<= '9') || str[i] == '+' || str[i] == '-'))
			return 0;
		int flag = 0;
		if (str[i] == '+')
		{
			flag = 0;
			i++;
		}
		else if (str[i] == '-')
		{
			flag = 1;
			i++;
		}
		if (!(str[i] >= '0' && str[i]<= '9'))
			return 0;
		while(i < str.length() && str[i] >= '0' && str[i]<= '9')
		{
			sum = sum * 10 + (str[i] - '0');
			i++;
			if (flag == 0)
			{
				if (sum > 0x7FFFFFFF)
					return 0x7FFFFFFF;
			}
			else
			{
				if (sum != 0)
					if (0 - sum < 0xFFFFFFFF80000000)
						return 0x80000000;
			}
		}
		if (flag == 0)
		{
			return sum;
		}
		else
		{
			if (sum == 0)
				return 0;
			else
				return 0 - sum;
		}
	}
};
