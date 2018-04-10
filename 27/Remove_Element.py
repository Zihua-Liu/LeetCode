class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        del_ele = 0
        for i in range(len(nums)):
        	if nums[i] == val:
        		nums[i] = 1 << 20
        		del_ele = del_ele + 1
        new_length = len(nums) - del_ele
        ptr = new_length
        for i in range(new_length):
        	if nums[i] == 1 << 20:
        		while True:
        			if nums[ptr] != 1 << 20:
        				nums[i] = nums[ptr]
        				ptr = ptr + 1
        				break
        			ptr = ptr + 1
        return new_length
