class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in range(len(strs)):
        	tmp = list(strs[i])
        	tmp.sort()
        	tmp = str(tmp)
        	if dic.has_key(tmp):
        		dic[tmp].append(strs[i])
        	else:
        		dic[tmp] = [strs[i]]
        result = []
        for ele in dic:
        	result.append(dic[ele])
        return result