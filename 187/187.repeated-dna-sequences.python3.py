#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (33.79%)
# Total Accepted:    102.4K
# Total Submissions: 302.9K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# Example:
# 
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# 
#
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hash_set = {}
        for i in range(len(s) - 9):
        	if s[i:i + 10] in hash_set.keys():
        		hash_set[s[i:i + 10]] += 1
        	else:
        		hash_set[s[i:i + 10]] = 1
        result = []
        for key in hash_set.keys():
        	if hash_set[key] > 1:
        		result.append(key)
        return result
        
