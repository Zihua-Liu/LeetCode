class Solution:
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		if n <= 0:
			return []

		# Initialize result matrix
		result = []
		for i in range(n):
			result.append([])
			for j in range(n):
				result[i].append(0)

		self.writeResult(result, 1, 0, 0, "right", n)
		return result

	def writeResult(self, result, value, row, col, direction, dim):
		result[row][col] = value
		if value == dim * dim:
			return

		if direction == "right":
			if col < dim - 1 and result[row][col + 1] == 0:
				self.writeResult(result, value + 1, row, col + 1, "right", dim)
			else:
				self.writeResult(result, value + 1, row + 1, col, "down", dim)

		if direction == "down":
			if row < dim - 1 and result[row + 1][col] == 0:
				self.writeResult(result, value + 1, row + 1, col, "down", dim)
			else:
				self.writeResult(result, value + 1, row, col - 1, "left", dim)

		if direction == "left":
			if col > 0 and result[row][col - 1] == 0:
				self.writeResult(result, value + 1, row, col - 1, "left", dim)
			else:
				self.writeResult(result, value + 1, row - 1, col, "up", dim)

		if direction == "up":
			if row > 0 and result[row - 1][col] == 0:
				self.writeResult(result, value + 1, row - 1, col, "up", dim)
			else:
				self.writeResult(result, value + 1, row, col + 1, "right", dim)

if __name__ == "__main__":
	sol = Solution()
	print(sol.generateMatrix(3))