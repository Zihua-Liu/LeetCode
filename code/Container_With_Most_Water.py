class Solution(object):
	def maxArea(self, height):
		left = 0
		right = len(height) - 1
		max_area = (right - left) * min(height[left], height[right])
		while left != right:
			if height[left] <= height[right]:
				left = left + 1
				if height[left] > height[left - 1]:
					tmp_area = (right - left) * min(height[left], height[right])
					if tmp_area > max_area:
						max_area = tmp_area
				else:
					continue
			else:
				right = right - 1
				if height[right] > height[right + 1]:
					tmp_area = (right - left) * min(height[left], height[right])
					if tmp_area > max_area:
						max_area = tmp_area
				else:
					continue
		return max_area
