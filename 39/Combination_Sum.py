import copy
class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		result = []
		candidates.sort()
		self.dfs(candidates, target, 0, [], result)
		return result

	def dfs(self, candidates, target, ptr, currrent_result, whole_result):

		if target == 0:
			print(currrent_result)
			whole_result.append(copy.deepcopy(currrent_result))
		if target < candidates[ptr]:
			return

		for i in range(ptr, len(candidates)):
			currrent_result.append(candidates[i])
			self.dfs(candidates, target - candidates[i], i, currrent_result, whole_result)
			currrent_result.pop()

		

s = Solution()
print(s.combinationSum([3,12,9,11,6,7,8,5,4], 15)) 		
