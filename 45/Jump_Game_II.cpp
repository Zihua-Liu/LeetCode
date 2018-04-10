class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int ret = 0;
        int curMax = 0;
        int curRch = 0;
        for(int i = 0; i < n; i ++)
        {
            if(curRch < i)
            {
                ret ++;
                curRch = curMax;
            }
            curMax = max(curMax, nums[i]+i);
        }
        return ret;
    }
};