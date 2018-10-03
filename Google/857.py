class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        quality_wage_ratio = [(q, w, w / q) for w, q in zip(wage, quality)]
        quality_wage_ratio.sort(key = lambda x: x[2])
        min_queue = [item[0] for item in quality_wage_ratio[0:K]]
        min_queue.sort(reverse = True)
        total_quality = sum(min_queue)
        ans = total_quality * quality_wage_ratio[K - 1][2]
        for i in range(K, len(quality_wage_ratio)):
        	if quality_wage_ratio[i][0] < min_queue[0]:
        		total_quality -= min_queue[0]
        		total_quality += quality_wage_ratio[i][0]
        		min_queue[0] = quality_wage_ratio[i][0]
        		min_queue.sort(reverse = True)
        		if total_quality * quality_wage_ratio[i][2] < ans:
        			ans = total_quality * quality_wage_ratio[i][2]
        return ans

sol = Solution()
print(sol.mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))



