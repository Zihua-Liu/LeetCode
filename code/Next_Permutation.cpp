class Solution {
public:
    void nextPermutation(vector<int>& nums) {
    	int size = nums.size();
    	int i_ptr = -1;
    	int j_ptr = -1;
        for (int length = 2; length <= size; length++)
        {
        	for (int i = 0; i <= size - length; i++)
        	{
        		if (nums[i] < nums[i + length - 1])
        		{
        			if (i > i_ptr)
        			{
        				i_ptr = i;
        				j_ptr = i + length - 1;
        			}
        			if (i == i_ptr)
        			{
        				if (nums[j_ptr] >= nums[i + length - 1])
        					j_ptr = i + length - 1;

        			}
        		}
        	}
        }
        if(i_ptr != -1)
        {
        	swap(nums[i_ptr], nums[j_ptr]);
        }

        for (int i = i_ptr + 1; i < size - 1; i++)
        {
        	for (int j = i + 1; j < size; j++)
        	{
        		if (nums[i] > nums[j])
        			swap(nums[i], nums[j]);
        	}
        }
        return;
    }
};