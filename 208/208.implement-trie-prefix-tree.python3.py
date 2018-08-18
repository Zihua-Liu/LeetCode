#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (32.76%)
# Total Accepted:    126.8K
# Total Submissions: 387K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#
class Node:
    def __init__(self):
        self.sons = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.sons.keys():
                current_node.sons[word[i]] = Node()
            current_node = current_node.sons[word[i]]
        current_node.sons["end"] = "end"

        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.sons.keys():
                return False
            current_node = current_node.sons[word[i]]
        if "end" not in current_node.sons.keys():
            return False
        return True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in current_node.sons.keys():
                return False
            current_node = current_node.sons[prefix[i]]
        return True

# trie = Trie();

# trie.insert("apple")
# print(trie.search("apple"))
# print(trie.search("app"))
# print(trie.startsWith("app"))
# trie.insert("app")   
# print(trie.search("app"))
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
