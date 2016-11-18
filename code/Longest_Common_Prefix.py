class Solution(object):
	def longestCommonPrefix(self, strs):
		length = 0
		while True:
			if len(strs) == 0:
				return ""
			if length == len(strs[0]):
				break
			flag = 1
			key = strs[0][length:length+1]
			for ele in strs:
				if ele[length:length+1] != key:
					flag = 0
					break
			if flag == 1:
				length = length + 1
			else:
				break;
		return strs[0][0:length]