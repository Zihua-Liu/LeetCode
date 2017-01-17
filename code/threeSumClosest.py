class Solution(object):
	def threeSumClosest(self, nums, target):
		nums.sort()
		gap = 1 << 20
		result = 0
		for i in range(0, len(nums) - 2):
			left = i + 1
			right = len(nums) - 1
			while left < right:
				tmp = nums[i] + nums[left] + nums[right]
				if tmp < target:
					if target - tmp < gap:
						gap = target - tmp
						result = tmp
					left = left + 1
				elif target < tmp:
					if tmp - target < gap:
						gap = tmp - target
						result = tmp
					right = right - 1
				else:
					return tmp
		return result