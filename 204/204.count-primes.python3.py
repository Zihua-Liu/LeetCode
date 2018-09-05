#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (27.02%)
# Total Accepted:    176K
# Total Submissions: 651.2K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = []
        record = [True for i in range(0, n + 1)]
        ans = 0
        for i in range(2, n):
            if record[i] == True:
                ans += 1
                prime.append(i)
            for num in prime:
                if num * i < n:
                    record[num * i] = False
                else:
                    break
        return ans

        
