class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        hash_set = {}
        for loc in stones:
        	hash_set[loc] = set()
        if stones[1] != 1:
        	return False
        hash_set[1].add(1)
        for loc in stones[1:]:
        	for step in hash_set[loc]:
        		if step - 1 > 0 and loc + step - 1 in hash_set:
        			hash_set[loc + step - 1].add(step - 1)
        		if loc + step in hash_set:
        			hash_set[loc + step].add(step)
        		if loc + step + 1 in hash_set:
        			hash_set[loc + step + 1].add(step + 1)
        if hash_set[stones[-1]] != set():
        	return True
        return False
sol = Solution()
print(sol.canCross([0,1,3,4,5,7,9,10,12]))