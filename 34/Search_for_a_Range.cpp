class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> v;
        if (nums.size() == 0)
        {
        	v.push_back(-1);
        	v.push_back(-1);
        	return v;
        }
        v.push_back(find_left(nums, 0, nums.size() - 1, target));
        v.push_back(find_right(nums, 0, nums.size() - 1, target));
        return v;
    }
    int find_left(vector<int>&nums, int left, int right, int target)
    {
    	if (left == right)
    	{
    		if(nums[left] == target)
    			return left;
    		else
    			return -1;
    	}
    	int mid = (left + right) / 2;
    	if (nums[mid] >= target)
    		return find_left(nums, left, mid, target);
    	else
    		return find_left(nums, mid + 1, right, target);
    }

    int find_right(vector<int>&nums, int left, int right, int target)
    {
    	if (left == right)
    	{
    		if(nums[left] == target)
    			return left;
    		else
    			return -1;
    	}
    	int mid = (left + right) / 2;
    	if (nums[mid] > target)
    		return find_right(nums, left, mid, target);
    	else if(nums[mid] == target)
    	{
    		if (mid < nums.size() - 1 && nums[mid + 1] == nums[mid])
    			return find_right(nums, mid + 1, right, target);
    		else
    			return find_right(nums, left, mid, target);
    	}
    	else
    		return find_right(nums, mid + 1, right, target);
    }
};
