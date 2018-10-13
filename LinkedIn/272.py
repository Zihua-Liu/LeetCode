# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ans = []
        self.inorder_traversal(root, target, k, ans)
        return ans
    
    def inorder_traversal(self, root, target, k, ans):
    	if root == None:
    		return None
    	self.add(ans, target, k, self.inorder_traversal(root.left, target, k, ans))
    	self.add(ans, target, k, root.val)
    	self.add(ans, target, k, self.inorder_traversal(root.right, target, k, ans))
    	return

    def add(self, ans, target, k, num):
    	if num == None:
    		return
    	ans.append(num)
    	if len(ans) <= k:
    		return
    	if target <= ans[0]:
    		ans.pop(-1)
    	elif ans[0] < target < ans[-1]:
    		if target - ans[0] < ans[-1] - target:
    			ans.pop(-1)
    		else:
    			ans.pop(0)
    	else:
    		ans.pop(0)