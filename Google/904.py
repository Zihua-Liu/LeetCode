class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if tree == []:
        	return 0
        cnt1 = [1]
        for i in range(1, len(tree)):
        	if tree[i] == tree[i - 1]:
        		cnt1.append(cnt1[i - 1] + 1)
        	else:
        		cnt1.append(1)
        cnt2 = [1]
        used = [tree[0]]
        i = 1
        while i < len(tree):
        	if tree[i] == tree[i - 1]:
        		cnt2.append(cnt2[i - 1] + 1)
        	else:
        		if len(used) < 2:
        			used.append(tree[i])
        			cnt2.append(cnt2[i - 1] + 1)
        		else:
        			if tree[i] in used:
        				cnt2.append(cnt2[i - 1] + 1)
        			else:
        				cnt2.append(cnt1[i - 1] + 1)
        				used = [tree[i - 1], tree[i]]
        	i += 1
        return max(cnt2)
