import copy
class Solution(object):
	def combinationSum2(self, candidates, target):
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
		    if currrent_result not in whole_result:
			    whole_result.append(copy.deepcopy(currrent_result))
		if ptr == len(candidates):
		    return
		if target < candidates[ptr]:
			return

		for i in range(ptr, len(candidates)):
			currrent_result.append(candidates[i])
			self.dfs(candidates, target - candidates[i], i + 1, currrent_result, whole_result)
			currrent_result.pop()

		

