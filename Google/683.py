class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        record = [False] * (len(flowers) + 1)
        for i in range(0, len(flowers)):
        	day = i + 1
        	record[flowers[i]] = True
        	if flowers[i] - k - 1 >= 1 and record[flowers[i] - k - 1] == True and (True not in record[flowers[i] - k: flowers[i]]):
        		return day
        	if flowers[i] + k + 1 <= len(flowers) and record[flowers[i] + k + 1] == True and (True not in record[flowers[i] + 1: flowers[i] + k + 1]):
        		return day
        return -1

sol = Solution()
print(sol.kEmptySlots([1, 2, 3], 1))