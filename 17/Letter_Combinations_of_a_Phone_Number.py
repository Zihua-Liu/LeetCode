class Solution(object):
    def letterCombinations(self, digits):
    	if digits == "":
    		return []
    	digits_to_letter = [[],[],["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], 
    						["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
    	result_len = 1
    	for i in range(len(digits)):
    		num = int(digits[i])
    		result_len = result_len * len(digits_to_letter[num])
    	result = []
    	for i in range(result_len):
    		k = i
    		result_str = ""
    		tmp_len = result_len
    		for j in range(len(digits)):
    			num = int(digits[j])
    			tmp_len = tmp_len / len(digits_to_letter[num])
    			result_str = result_str + digits_to_letter[num][int(k / tmp_len)]
    			k = int(k % tmp_len)
    		result.append(result_str)
    	return result



