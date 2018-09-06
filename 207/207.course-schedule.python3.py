#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (34.69%)
# Total Accepted:    144.8K
# Total Submissions: 417.3K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        for prerequisite_pair in prerequisites:
        	in_degree[prerequisite_pair[0]] += 1
        	graph[prerequisite_pair[1]].append(prerequisite_pair[0])
        ans = 0
        queue = []
        for i in range(numCourses):
        	if in_degree[i] == 0:
        		queue.append(i)
        while queue != []:
        	course_index = queue[0]
        	queue.pop(0)
        	ans += 1
        	for course in graph[course_index]:
        		in_degree[course] -= 1
        		if in_degree[course] == 0:
        			queue.append(course)
        if ans == numCourses:
        	return True 
        else:
        	return False

        
