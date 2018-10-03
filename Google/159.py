class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
        	return len(s)
        most1 = [1]
        if s[1] == s[0]:
        	most1.append(2)
        else:
        	most1.append(1)
        most2 = [1, 2]
        for i in range(2, len(s)):
        	most2.append(1)
        	if s[i] == s[i - 1]:
        		most1.append(1 + most1[i - 1])
        	else:
        		most1.append(1)
        	used = [s[i]]
        	j = i - 1
        	while j >= 0:
        		if len(used) == 2 and s[j] not in used:
        			break
        		most2[i] += most1[j]
        		if s[j] not in used:
        			used.append(s[j])
        		j -= most1[j]
        return max(most2)

sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"))