class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = []
        c.append(nums[0])
        for i in range(1, len(nums)):
        	if c[i - 1] + nums[i] > nums[i]:
        		c.append(c[i - 1] + nums[i])
        	else:
        		c.append(nums[i])
        result = nums[0]
        for i in range(len(nums)):
        	if result < c[i]:
        		result = c[i]
        return result