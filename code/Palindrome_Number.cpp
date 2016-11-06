class Solution
{
public:
	bool isPalindrome(int x)
	{
		if (x < 0)
			return false;
		int left = (int)log10(x), right = 0;
		while(left > right)
		{
			if ((x % (int)(pow(10, left + 1))/ (int)(pow(10, left))) != (x % (int)(pow(10, right + 1))/ (int)(pow(10, right))))
				return false;
			left--;
			right++;
		}
		return true;
	}
};