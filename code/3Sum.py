class Solution(object):
	def threeSum(self, nums):
		def find(nums, left, right, remain):
			if left == right:
				if nums[left] != remain:
					return -1
				else:
					return left
			else:
				temp = nums[int((left + right) / 2)]
				if remain > temp:
					return find(nums, int((left + right) / 2) + 1, right, remain)
				else:
					return find(nums, left, int((left + right) / 2), remain)
		result = []
		nums.sort()
		for i in range(len(nums) - 2):
			if nums[i] + nums[i+1] > 0:
				break
			if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] < 0:
				continue
			for j in range(i + 1, len(nums) - 1):
				add1 = nums[i]
				add2 = nums[j]
				if add1 + add2 + nums[j + 1] > 0:
					break
				if add1 + add2 + nums[len(nums) - 1] < 0:
					continue
				remain = 0 - add1 - add2
				if [add1, add2, remain] in result:
					continue
				if remain < nums[j + 1] or remain > nums[len(nums) - 1]:
					continue
				if find(nums, j + 1, len(nums) - 1, remain) != -1:
					result.append([add1, add2, remain])
		return result

