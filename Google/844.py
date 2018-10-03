class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_list = list(S)
        T_list = list(T)
        return self.filter(S_list) == self.filter(T_list)

    def filter(self, word_list):
    	for i in range(len(word_list)):
    		if word_list[i] == "#":
    			j = i - 1
    			while j >= 0 and word_list[j] == "#":
    				j -= 1
    			if j >= 0:
    				word_list[j] = "#"
    	ans = ""
    	for char in word_list:
    		if char != "#":
    			ans += char
    	return ans