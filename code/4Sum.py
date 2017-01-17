class Solution(object):
    def fourSum(self, nums, target):
    	nums.sort()
    	result = []
    	for i in range(0, len(nums) - 3):
    		for j in range(i + 1, len(nums) - 2):
    			left = j + 1
    			right = len(nums) - 1
    			while left < right:
    				tmp = nums[i] + nums[j] + nums[left] + nums[right]
    				if tmp < target:
    					left = left + 1
    				elif target < tmp:
    					right = right - 1
    				else:
    					result.append([nums[i], nums[j], nums[left], nums[right]])
    					left = left + 1
    					if nums[i] + nums[j] + nums[left] + nums[right] > target:
    						left = left - 1
    						right = right - 1
    	return result

s = Solution()
print(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0))