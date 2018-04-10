/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int * record = malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; i++)
        record[i] = nums[i];
    for (int i = 0; i < numsSize - 1; i++)
    {
        for (int j = i + 1; j < numsSize; j++)
        {
            if (nums[i] > nums[j])
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
    for (int i = 0; i < numsSize; i++)
    {
        int left = i + 1, right = numsSize - 1, tar = target - nums[i];
        while(nums[left] <= tar && nums[right] >= tar)
        {
            int mid = (left + right) / 2;
            if (nums[mid] == tar)
            {
                int * result = malloc(2 * sizeof(int));
                for (int k = 0; k < numsSize; k++)
                {
                    if (record[k] == nums[i])
                    {
                        result[0] = k;
                        record[k] = 1 << 31;
                        break;
                    }
                }
                for (int k = 0; k < numsSize; k++)
                {
                    if (record[k] == nums[mid])
                        result[1] = k;
                }
                if (result[0] > result[1])
                {
                    int temp = result[0];
                    result[0] = result[1];
                    result[1] = temp;
                }
                return result;
            }
            else if(nums[mid] < tar)
            {
                left = mid + 1;
                continue;
            }
            else
            {
                right = mid;
                continue;
            }
        }
    }
    return NULL;
}
