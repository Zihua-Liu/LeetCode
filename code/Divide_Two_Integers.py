class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if dividend == -2147483648 and divisor == -1:
        	return MAX_INT
        result = 0
        flag = 0
        if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0):
        	flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
        	tmp = 0
        	while True:
        		if (divisor << tmp) <= dividend and (divisor << (tmp + 1)) > dividend:
        			break
        		tmp = tmp + 1
        	result = result + int(pow(2, tmp))
        	dividend = dividend - (divisor << tmp)
        if flag == 0:
        	return 0 - result
        else:
        	return result

