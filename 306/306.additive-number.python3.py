#
# [306] Additive Number
#
# https://leetcode.com/problems/additive-number/description/
#
# algorithms
# Medium (27.89%)
# Total Accepted:    34.6K
# Total Submissions: 124.1K
# Testcase Example:  '"112358"'
#
# Additive number is a string whose digits can form additive sequence.
# 
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum
# of the preceding two.
# 
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
# 
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
# 
# Example 1:
# 
# 
# Input: "112358"
# Output: true 
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5,
# 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# Example 2:
# 
# 
# Input: "199100199"
# Output: true 
# Explanation: The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
# 
# Follow up:
# How would you handle overflow for very large input integers?
#
class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num) - 1):
            for j in range(i, len(num) - 1):
                num1 = num[:i]
                num2 = num[i:j + 1]
                if len(num1) > 1 and num1[0] == "0":
                    continue
                if len(num2) > 1 and num2[0] == "0":
                    continue
                num1 = int(num1)
                num2 = int(num2)
                print(num1)
                print(num2)
                print()
                sum2 = num1 + num2
                if sum2 != int(num[j + 1: j + 1 + len(str(sum2))]):
                    continue
                ptr = i
                len1 = j + 1 - i
                len2 = len(str(sum2))
                success = True
                while ptr + len1 + len2 < len(num):
                    num1 = num[ptr:ptr + len1]
                    num2 = num[ptr + len1:ptr + len1 + len2]
                    print(num1)
                    print(num2)
                    print()
                    if len(num2) > 1 and num2[0] == "0":
                        success = False
                        break
                    num1 = int(num1)
                    num2 = int(num2)
                    sum2 = num1 + num2
                    if sum2 != int(num[ptr + len1 + len2:ptr + len1 + len2 + len(str(sum2))]):
                        success = False
                        break
                    ptr = ptr + len1
                    len1 = len2
                    len2 = len(str(sum2))
                if success:
                    return True
        return False
sol = Solution()
print(sol.isAdditiveNumber("123"))


