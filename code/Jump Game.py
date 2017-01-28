class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = []
        c.append(nums[0])
        for i in range(1, len(nums)):
        	if c[i - 1] >= i:
        		c.append(max(i + nums[i], c[i - 1]))
        	else:
        		return False
        return True
