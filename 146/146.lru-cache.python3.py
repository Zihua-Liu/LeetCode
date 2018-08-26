#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (20.90%)
# Total Accepted:    195.5K
# Total Submissions: 930.9K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#
class Entry:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash_set = {}
        self.head = None
        self.tail = None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_set.keys() or self.hash_set[key] == None:
            return -1
        entry = self.hash_set[key]
        if self.tail != None and entry.key == self.tail.key:
            if self.tail.prev != None:
                self.tail = self.tail.prev
                self.tail.next = None
        if entry.prev != None:
            entry.prev.next = entry.next
        if entry.next != None:
            entry.next.prev = entry.prev
        if self.head != entry:
            entry.next = self.head
        if entry.next != None:
            entry.next.prev = entry
        entry.prev = None
        self.head = entry
        return entry.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.hash_set.keys() or self.hash_set[key] == None:
            self.hash_set[key] = Entry(key, value, None, self.head)
            if self.head == None:
                self.head = self.hash_set[key]
            else:
                self.head.prev = self.hash_set[key]
                self.head = self.hash_set[key]
            if self.tail == None:
                self.tail = self.hash_set[key]

            if len(self.hash_set.keys()) > self.capacity:
                if self.tail.prev != None:
                    self.tail.prev.next = None
                self.hash_set[self.tail.key] = None
                self.tail = self.tail.prev
                if self.capacity == 1:
                    self.head = self.tail
        else:
            entry = self.hash_set[key]
            entry.value = value
            if self.tail != None and entry.key == self.tail.key:
                if self.tail.prev != None:
                    self.tail = self.tail.prev
            if entry.prev != None:
                entry.prev.next = entry.next
            if entry.next != None:
                entry.next.prev = entry.prev
            if self.head != entry:
                entry.next = self.head
            if entry.next != None:
                entry.next.prev = entry
            entry.prev = None
            self.head = entry

