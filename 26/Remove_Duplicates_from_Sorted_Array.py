class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
        	return 0
        result = len(nums)
        new_len = 1
        ptr = nums[0]
        for i in range(1, len(nums)):
        	if ptr == nums[i]:
        		result = result - 1
        	else:
        		nums[new_len] = nums[i]
        		ptr = nums[i]
        		new_len = new_len + 1
        #nums = list(set(nums))
        return result