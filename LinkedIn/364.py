# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        max_depth = self.getDepth(nestedList)
        print(max_depth)
        return self.calculate(nestedList, max_depth, 0)

        

    def getDepth(self, nestedList):
    	max_depth = 1
    	for item in nestedList:
    		if not item.isInteger():
    			max_depth = max(max_depth, self.getDepth(item.getList()) + 1)
    	return max_depth

    def calculate(self, nestedList, max_depth, current_level):
    	ans = 0
    	for item in nestedList:
    		if not item.isInteger():
    			ans += self.calculate(item.getList(), max_depth, current_level + 1)
    		else:
    			ans += (max_depth - current_level) * item.getInteger()
    	return ans
