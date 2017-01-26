class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 0
        if n < 0:
        	flag = 1
        	n = -n
        binary = []
        while True:
        	binary.append(n % 2)
        	n = int(n / 2)
        	if n == 0:
        		break
        record = []
        tmp = x
        for i in range(len(binary)):
        	record.append(tmp)
        	tmp = tmp * tmp
        result = 1.0
        for i in range(len(binary)):
        	if binary[i] == 1:
        		result = result * record[i]
        if flag == 1:
        	return 1.0 / result
        return result