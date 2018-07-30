#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (37.37%)
# Total Accepted:    48.4K
# Total Submissions: 128.9K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
# 
# 
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
# 
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
# 
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# 
# 
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# 
# 
# Input: "1,#"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: "9,#,#,1"
# Output: false
# 
#
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder_character = preorder.split(",")
        my_stack = []
        for i in range(0, len(preorder_character)):
            if preorder_character[i] != "#":
                my_stack.append(preorder_character[i])
            else:
                my_stack.append(preorder_character[i])
                while True:
                    if len(my_stack) < 3:
                        break
                    if not (my_stack[-1] == "#" and my_stack[-2] == "#"):
                        break
                    if my_stack[-3] == "#":
                        return False
                    else:
                        my_stack.pop()
                        my_stack.pop()
                        my_stack[-1] = "#"
        if my_stack == ["#"]:
            return True
        else:
            return False
        
