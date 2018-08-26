#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.27%)
# Total Accepted:    70.1K
# Total Submissions: 381K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# Example 1:
# 
# 
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# 
# Example 2:
# 
# 
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# 
# 
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# 
# 
#
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
        	return "0"
        minus = False
        minus = not minus if numerator < 0 else minus
        minus = not minus if denominator < 0 else minus
       	numerator = abs(numerator)
       	denominator = abs(denominator)
        result = "-" if minus else ""
        integer_part = numerator // denominator
        result += str(integer_part)
        remainer = numerator % denominator
        if remainer == 0:
        	return result
        else:
        	result += "."
        remainer_record = {}
        demical_part = ""
        while remainer != 0 and remainer not in remainer_record.keys():
       		remainer_record[remainer] = len(demical_part)
        	remainer *= 10
        	demical_part += str(remainer // denominator)
        	remainer %= denominator
        if remainer == 0:
        	return result + demical_part
        else:
        	return "{}{}({})".format(result, 
        							demical_part[:remainer_record[remainer]], 
        							demical_part[remainer_record[remainer]:])
sol = Solution()
print(sol.fractionToDecimal(1, 6))
        
