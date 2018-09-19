#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (47.28%)
# Total Accepted:    61.5K
# Total Submissions: 129.9K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
# 
# Example 1:
# 
# 
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# Example 2:
# 
# 
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
# 
#
class Node:
	def __init__(self, left, right, op, val):
		self.left = left
		self.right = right
		self.op = op
		self.val = val

	def get_val(self):
		if self.val != None:
			return self.val
		if self.op == "+":
			self.val = self.left.get_val() + self.right.get_val()
		elif self.op == "-":
			self.val = self.left.get_val() - self.right.get_val()
		else:
			self.val = self.left.get_val() * self.right.get_val()
		return self.val

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        trees = self.build_trees(input)
        ans = [tree.get_val() for tree in trees]
        return ans

    def build_trees(self, input):
    	ans = []
    	for i in range(len(input)):
    		if input[i] in ["+", "-", "*"]:
    			left_trees = self.build_trees(input[:i])
    			right_trees = self.build_trees(input[i + 1:])
    			for left_tree in left_trees:
    				for right_tree in right_trees:
    					ans.append(Node(left_tree, right_tree, input[i], None))
    	if ans == []:
    		ans.append(Node(None, None, None, int(input)))
    	return ans

sol = Solution()
print(sol.diffWaysToCompute("2*3-4*5"))
