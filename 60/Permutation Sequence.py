class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        assist_array = []
        visit = []
        assist_array.append(1)
        visit.append(False)
        for i in range(1, n + 1):
        	visit.append(False)
        	assist_array.append(i * assist_array[i - 1])
        for i in range(1, n + 1):
        	remain = k % assist_array[n - i]
        	if remain > 0:
        		digit = self.findMinNotUse(visit, int(k / assist_array[n - i]) + 1)
        		k = k % assist_array[n - i]
        	else:
        		digit = self.findMinNotUse(visit, int(k / assist_array[n - i]))
        		k = assist_array[n - i]
        	result = result + str(digit)
        return result





    def findMinNotUse(self, visit, cnt):
    	for i in range(1, len(visit)):
    		if visit[i] == False:
    			cnt = cnt - 1
    			if cnt == 0:
    				visit[i] = True
    				return i

if __name__ == "__main__":
	sol = Solution()
	print(sol.getPermutation(3, 6))