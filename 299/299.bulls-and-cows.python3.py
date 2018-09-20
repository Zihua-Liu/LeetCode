#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Medium (36.91%)
# Total Accepted:    75.3K
# Total Submissions: 203.9K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's

# 
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# 
# Output: "1A3B"
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# 
# Output: "1A1B"
# 
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
# 
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        hash_set_secret = {}
        hash_set_guess = {}
        for i in range(len(secret)):
        	sec = secret[i]
        	gue = guess[i]
        	if sec == gue:
        		bull += 1
        	if sec not in hash_set_secret:
        		hash_set_secret[sec] = 1
        	else:
        		hash_set_secret[sec] += 1
        	if sec not in hash_set_guess:
        		hash_set_guess[sec] = 0

        	if gue not in hash_set_guess:
        		hash_set_guess[gue] = 1
        	else:
        		hash_set_guess[gue] += 1
        tot = 0
        for sec in hash_set_secret.keys():
        	tot += min(hash_set_secret[sec], hash_set_guess[sec])
        cow = tot - bull
        return "{}A{}B".format(bull, cow)