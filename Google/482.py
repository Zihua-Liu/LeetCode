class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-", "").upper()
        first_len = len(s) % K
        if first_len == 0:
        	first_len = K
        ans = s[:first_len]
        for i in range(first_len, len(s), K):
        	ans += "-{}".format(s[i:i+K])
        return ans

sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))