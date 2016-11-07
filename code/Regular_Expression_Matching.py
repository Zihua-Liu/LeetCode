class Solution(object):
	def isMatch(self, s, p):
		if p[-1:] != "*" and p[-1:] != ".":
			if s[-1:] != p[-1:]:
				return False
		if s == "" and p =="":
			return True
		if s == p:
			return True
		if s == "" and p != "":
			if p[1:2] != "*":
				return False
			else:
				return self.isMatch(s, p[2:])
		if s != "" and p == "":
			return False
		if s[0:1] == p[0:1]:
			if p[1:2] != "*":
				return self.isMatch(s[1:], p[1:])
			else:
				return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
		else:
			if p[1:2] != "*":
				if p[0:1] == ".":
					return self.isMatch(s[1:], p[1:])
				else:
					return False
			else:
				if p[0:1] == ".":
					return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
				else:
					return self.isMatch(s, p[2:])

					