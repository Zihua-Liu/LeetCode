#include <iostream>
#include <memory.h>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        int* number1 = new int[num1.length() + num2.length()];
        int* number2 = new int[num1.length() + num2.length()];
        memset(number1, 0, num1.length() + num2.length());
        memset(number2, 0, num1.length() + num2.length());
        for (int i = 0; i < num1.length(); i++)
        	number1[i] = num1[num1.length() - 1 - i] - '0';
        for (int i = 0; i < num2.length(); i++)
        	number2[i] = num2[num2.length() - 1 - i] - '0';
        int * tmp;
        int * result;
        for (int i = 0; i < num2.length(); i++)
        {
        	tmp = multi(number1, number2[i], num1.length() + i);
        	result = add(result, tmp, num1.length() + i + 1);
        	for (int j = num1.length() + i; j > 0 + i; j--)
        		number1[j] = number1[j-1];
        	number1[i] = 0;
        }
        int i = num1.length() + num2.length();
        while(result[i] == 0)
        	i--;
        char* return_string = new char[i + 1];
        int len = i + 1;
        while(i >= 0)
        {
        	return_string[len - i - 1] = result[i] + '0';
        	i--;
        }
        return (string)return_string;
    }

    int* multi(int* a, int b, int length)
    {
    	int * result = new int[length+1];
    	memset(result, 0, length+1);
    	for (int i = 0; i < length; i++)
    	{
    		result[i] += (a[i] * b) % 10;
    		result[i+1] += (a[i] * b) / 10;
    	}
    	return result;
    }
    int* add(int* a, int* b, int length)
    {
    	int * result = new int[length+1];
    	memset(result, 0, length+1);
    	for (int i = 0; i < length; i++)
    	{
    		result[i] += (a[i] + b[i]) % 10;
    		result[i+1] += (a[i] + b[i]) / 10;
    	}
    	return result;
    }
};

int main()
{
	Solution* s = new Solution();
	cout << s->multiply("0", "0");
	return 0;
}