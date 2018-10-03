class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        union_find = UnionFind(equations)
        for equation, value in zip(equations, values):
            op1, op2 = equation
            union_find.union(op1, op2, value)
        ans = []
        for query in queries:
            op1, op2 = query
            root1, product1 = union_find.find(op1)
            root2, product2 = union_find.find(op2)
            if root1 != None and root2 != None and root1 == root2:
                ans.append(product2 / product1)
            else:
                ans.append(-1.0)
        return ans

class UnionFind:
    def __init__(self, equations):
        self.parents = {}
        for equation in equations:
            self.parents[equation[0]] = (equation[0], 1.0)
            self.parents[equation[1]] = (equation[1], 1.0)
        return

    def find(self, op):
        if op not in self.parents:
            return (None, None)
        if self.parents[op][0] == op:
            return self.parents[op]
        root, product = self.find(self.parents[op][0])
        return (root, product * self.parents[op][1])

    def union(self, op1, op2, value):
        root_op1 = self.find(op1)
        root_op2 = self.find(op2)
        if root_op1[0] == root_op2[0]:
            return
        else:
            self.parents[root_op2[0]] = (root_op1[0], value * root_op1[1] / root_op2[1])
        return

sol = Solution()
print(sol.calcEquation([["a","e"],["b","e"]] ,[4.0,3.0] ,[["a","b"],["e","e"],["x","x"]]))

        