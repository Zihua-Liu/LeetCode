class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.insert_nums = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        try:
            self.insert_nums[number] += 1
        except:
            self.insert_nums[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.insert_nums.keys():
            try:
                if value - num == num:
                    if self.insert_nums[value - num] > 1:
                        return True
                    else:
                        continue
                else:
                    if self.insert_nums[value - num]:
                        return True
            except:
                continue
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)