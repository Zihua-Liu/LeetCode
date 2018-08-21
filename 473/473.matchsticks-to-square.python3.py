#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (35.44%)
# Total Accepted:    18.6K
# Total Submissions: 52.4K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
# 
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
# 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Note:
# 
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# 
# 
#
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 4 != 0 or nums == []:
        	return False
        nums.sort(reverse = True)
        return self.dfs(nums, sum(nums) // 4, [], 0, [])
        

    def dfs(self, nums, target, record, result, series):
    	if len(record) == len(nums) and result == 4:
    		return True

    	if target == 0:
    		return self.dfs(nums, sum(nums) // 4, record, result + 1, [])

    	if len(record) == len(nums) or result == 4:
    		return False

    	if target < 0:
    		return False
    	
    	for i in range(len(nums)):
    		if series != [] and i < series[-1]:
    			continue
    		if i not in record:
    			record.append(i)
    			series.append(i)
    			if self.dfs(nums, target - nums[i], record, result, series):
    				return True
    			record.pop()
    			series.pop()
    	return False
sol = Solution()
print(sol.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))



        
