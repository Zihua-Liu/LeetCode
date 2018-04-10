class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.dfs("1", n, 1)

    def dfs(self, s, n, count):
    	if count == n:
    		return s
    	result = ""
    	tmp = s[0]
    	i = 0
    	cnt = 0
    	while i < len(s):
    		if tmp == s[i]:
    			cnt = cnt + 1
    			i = i + 1
    		else:
    			result = result + str(cnt) + tmp
    			tmp = s[i]
    			cnt = 0
    	result = result + str(cnt) + tmp
    	return self.dfs(result, n, count + 1)
