class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return find_left(nums, 0, nums.size() - 1, target);
    }
    int find_left(vector<int>&nums, int left, int right, int target)
    {
    	if (left == right)
    	{
    		if(nums[left] == target)
    			return left;
    		else if (nums[left] < target)
    			return left + 1;
    		else
    			return left;
    		
    	}
    	int mid = (left + right) / 2;
    	if (nums[mid] >= target)
    		return find_left(nums, left, mid, target);
    	else
    		return find_left(nums, mid + 1, right, target);
    }
};