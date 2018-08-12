#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (34.73%)
# Total Accepted:    85.4K
# Total Submissions: 246K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分打劫第一家和不打劫第一家两种情况考虑，做两次动态规划
        if nums == []:
            return 0
        if len(nums) <= 3:
            return max(nums)

        nums_choose_head = nums[2:-1]
        if len(nums_choose_head) < 3:
            result_choose_head = max(nums_choose_head) + nums[0]
        else:
            record = nums_choose_head[0:2]  # record[i]代表必须包括从头打劫，且必须包含nums[i]所能获得的最大价值
            for i in range(2, len(nums_choose_head)):
                current_value = nums_choose_head[i]
                for j in range(0, i - 1):
                    if nums_choose_head[i] + record[j] > current_value:
                        current_value = nums_choose_head[i] + record[j]
                record.append(current_value)
            result_choose_head = max(record) + nums[0]

        nums_not_choose_head = nums[1:]
        if len(nums_not_choose_head) < 3:
            result_not_choose_head = max(nums_not_choose_head)
        else:
            record = nums_not_choose_head[0:2]  # record[i]代表必须包括从头打劫，且必须包含nums[i]所能获得的最大价值
            for i in range(2, len(nums_not_choose_head)):
                current_value = nums_not_choose_head[i]
                for j in range(0, i - 1):
                    if nums_not_choose_head[i] + record[j] > current_value:
                        current_value = nums_not_choose_head[i] + record[j]
                record.append(current_value)
            result_not_choose_head = max(record)
        return max(result_choose_head, result_not_choose_head)

        
