class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hash_set = {}
        for i, word in enumerate(words):
            if word not in self.hash_set:
                self.hash_set[word] = [i]
            else:
                self.hash_set[word].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.hash_set[word1]
        list2 = self.hash_set[word2]
        ans = 1 << 29
        for num in list1:
            tmp = self.binary_search(num, list2)
            if tmp < ans:
                ans = tmp
        return ans

    def binary_search(self, target, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return 0
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return 0
        elif nums[left] < target:
            if left == len(nums) - 1:
                return target - nums[left]
            else:
                return min(target - nums[left], abs(target - nums[left + 1]))
        else:
            if left == 0:
                return nums[left] - target
            else:
                return min(nums[left] - target, abs(nums[left - 1] - target))
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)