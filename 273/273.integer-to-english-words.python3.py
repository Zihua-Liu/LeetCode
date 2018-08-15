#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (22.95%)
# Total Accepted:    66.7K
# Total Submissions: 289.2K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#
class Solution:
    single_digit = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"
                    , 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    double_digit = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen"
                    , 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 2:"Twenty"
                    , 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty"
                    , 9:"Ninety"}

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        result = ""
        i = 0
        while num > 0:
            tmp_result = self.threeDigitNumberToWords(num % 1000)
            if i == 1 and tmp_result != "":
                tmp_result = "{} Thousand ".format(tmp_result)
            elif i == 2 and tmp_result != "":
                tmp_result = "{} Million ".format(tmp_result)
            elif i == 3 and tmp_result != "":
                tmp_result = "{} Billion ".format(tmp_result)
            result = tmp_result + result
            num = int(num / 1000)
            i += 1
        if result[0] == " ":
            result = result[1:]
        if result[-1] == " ":
            result = result[:-1]
        return result

    def threeDigitNumberToWords(self, num):
        result = ""
        if num > 99:
            result += "{} {}".format(self.single_digit[int(num / 100)], "Hundred")
        num = num % 100
        if num > 9 and num < 20:
            result += " {}".format(self.double_digit[num])
            if len(result) > 0 and result[0] == " ":
                result = result[1:]
            if len(result) > 0 and result[-1] == " ":
                result = result[:-1]
            return result
        elif num >= 20:
            result += " {}".format(self.double_digit[int(num / 10)])
        num = num % 10
        if num != 0:
            result += " {}".format(self.single_digit[num])
        if len(result) > 0 and result[0] == " ":
            result = result[1:]
        if len(result) > 0 and result[-1] == " ":
            result = result[:-1]
        return result
sol = Solution()
print(sol.numberToWords(1234567891))



        
