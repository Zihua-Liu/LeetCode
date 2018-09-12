#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (26.82%)
# Total Accepted:    86.5K
# Total Submissions: 322.3K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#
class Node:

    def __init__(self, val):
        self.val = val
        self.sons = []

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

        
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for i in range(len(word)):
            find = False
            for son in ptr.sons:
                if son == None:
                    continue
                if word[i] == son.val:
                    find = True
                    ptr = son
                    break
            if not find:
                son = Node(word[i])
                ptr.sons.append(son)
                ptr = son
        if None not in ptr.sons:
            ptr.sons.append(None)
        return



        
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)

    def dfs(self, word, node):
        if word == "":
            if None in node.sons:
                return True
            else:
                return False
        char = word[0]
        if char == ".":
            for son in node.sons:
                if son == None:
                    continue
                if self.dfs(word[1:], son):
                    return True
            return False
        else:
            for son in node.sons:
                if son == None:
                    continue
                if son.val == char:
                    return self.dfs(word[1:], son)
            return False


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
