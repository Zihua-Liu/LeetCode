#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.33%)
# Total Accepted:    111.9K
# Total Submissions: 424.9K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# 
# click to show corner cases.
# 
# Corner Cases:
# 
# 
# 
# 
# 
# 
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# 
#
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path.endswith("/..") or path.endswith("/."):
        	path += "/"
        while "/../" in path or "/./" in path:
	        path = path.replace("/../", "/&/")
	        path = path.replace("/./", "//")
        path_list = path.split('/')
        stack = []
        for item in path_list:
        	if len(item) > 0:
        		if item != "&":
        			stack.append(item)
        		else:
        			if len(stack) > 0:
        				stack.pop()
        result = ""
        for item in stack:
        	result += "/" + item
        if result == "":
        	return "/"

        return result













        
