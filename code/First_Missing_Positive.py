class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
        	if nums[i] != i + 1 and nums[i] > 0 and nums[i] <= len(nums):
        		m = nums[i]
        		n = nums[i] - 1
        		q = nums[nums[i] - 1]
        		nums[n] = m
        		nums[i] = q
        		if nums[i] <= 0 or m == q:
        			i = i + 1
        	else:
        		i = i + 1

        for i in range(len(nums)):
        	if nums[i] != i + 1:
        		return i + 1
        return len(nums) + 1