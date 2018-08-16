#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (32.06%)
# Total Accepted:    209.6K
# Total Submissions: 642.2K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_ele = None
        self.min_index_series =[]
        self.stack =[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min_ele == None or self.min_ele > x:
            self.min_ele = x
            self.min_index_series.append(len(self.stack))
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) - 1 == self.min_index_series[-1]:
            self.min_index_series.pop()
            if self.min_index_series != []:
                self.min_ele = self.stack[self.min_index_series[-1]]
            else:
                self.min_ele = None
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_ele
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
