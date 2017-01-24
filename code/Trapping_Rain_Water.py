class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		i = 0
		total_vol = 0
		flag = 0
		while i < len(height):
			current_height = height[i]
			tmp_vol = 0
			j = i + 1
			maxium = 0
			while j < len(height):
				if height[j] >= height[i]:
					break
				tmp_vol = tmp_vol + height[i] - height[j]
				if height[j] > maxium:
					maxium = height[j]
				j = j + 1

			if j != len(height):
				flag = 0
				total_vol = total_vol + tmp_vol
				i = j
				continue
			if j == len(height) and flag == 0:
				height[i] = maxium
				flag = 1
				continue
			else:
				flag = 0
				i = i + 1
		return total_vol
