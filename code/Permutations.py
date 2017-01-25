import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        record = []
        for i in range(len(nums)):
        	record.append(False)
        total_result = []
        self.dfs(nums, len(nums), 0, [], total_result, record)
        return total_result
    def dfs(self, nums, length, cnt, current_result, total_result, record):
    	if cnt == length:
    		total_result.append(copy.deepcopy(current_result))
    		return
    	for i in range(length):
    		if record[i] == False:
    			current_result.append(nums[i])
    			record[i] = True
    			self.dfs(nums, length, cnt+1, current_result, total_result, record)
    			record[i] = False
    			current_result.pop()
