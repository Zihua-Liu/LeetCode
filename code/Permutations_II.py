import copy
class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		record = []
		for i in range(len(nums)):
			record.append(False)
		total_result = []
		nums.sort()
		self.dfs(nums, len(nums), 0, [], total_result, record)
		return total_result
	def dfs(self, nums, length, cnt, current_result, total_result, record):
		if cnt == length:
			if current_result not in total_result:
				total_result.append(copy.deepcopy(current_result))
			return
		for i in range(length):
			if i > 0 and nums[i] == nums[i-1] and record[i-1] == False:
				continue
			if record[i] == False:
				current_result.append(nums[i])
				record[i] = True
				self.dfs(nums, length, cnt+1, current_result, total_result, record)
				record[i] = False
				current_result.pop()
s = Solution()
print(s.permuteUnique([1,1,2]))