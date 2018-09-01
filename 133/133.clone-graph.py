#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (25.18%)
# Total Accepted:    165.8K
# Total Submissions: 658.7K
# Testcase Example:  '{}'
#
# 
# Clone an undirected graph. Each node in the graph contains a label and a list
# of its neighbors.
# 
# 
# 
# 
# OJ's undirected graph serialization:
# 
# 
# Nodes are labeled uniquely.
# 
# 
# We use # as a separator for each node, and , as a separator for node label
# and each neighbor of the node.
# 
# 
# 
# 
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# 
# 
# The graph has a total of three nodes, and therefore contains three parts as
# separated by #.
# 
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
# self-cycle.
# 
# 
# 
# 
# Visually, the graph looks like the following:
# 
# ⁠      1
# ⁠     / \
# ⁠    /   \
# ⁠   0 --- 2
# ⁠        / \
# ⁠        \_/
# 
# 
# 
# 
#
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
    	if node == None:
    		return None
    	hash_set = {}
    	queue = [node]
    	while queue != []:
    		head = queue[0]
    		if head.label not in hash_set.keys():
    			hash_set[head.label] = UndirectedGraphNode(head.label)
    		for neighbor in head.neighbors:
    			if neighbor.label not in hash_set.keys():
    				queue.append(neighbor)
    				hash_set[neighbor.label] = UndirectedGraphNode(neighbor.label)
    			hash_set[head.label].neighbors.append(hash_set[neighbor.label])
    		queue.pop(0)
    	return hash_set[node.label]
        
