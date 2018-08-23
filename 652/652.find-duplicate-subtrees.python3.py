#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (38.67%)
# Total Accepted:    19.2K
# Total Submissions: 49.4K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# Example 1: 
# 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# The following are two duplicate subtrees:
# 
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# and
# 
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
#
class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        result = []
        self.dfs(root, {}, result)
        return result

    def dfs(self, root, record, result):
        if root == None:
            return [None]
        series = []
        series.append(root.val)
        series += self.dfs(root.left, record, result)
        series += self.dfs(root.right, record, result)
        if str(series) in record.keys():
            if record[str(series)] == 1:
                record[str(series)] = 2
                result.append(root)
        else:
            record[str(series)] = 1
        return series

        
