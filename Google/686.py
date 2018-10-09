class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(list(A)) != set(list(B)):
        	for char in B:
        		if char not in A:
        			return -1
        for i in range(0, len(A)):
        	if A[i] != B[0]:
        		continue
        	k = ((len(B) - len(A) + i) // len(A)) + 1 if (len(B) - len(A) + i) % len(A) == 0 else ((len(B) - len(A) + i) // len(A)) + 2
        	tmp_A = A * k
        	if B in tmp_A:
        		return k
        return -1
sol = Solution()
print(sol.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba"))


