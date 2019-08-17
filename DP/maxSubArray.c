#include <stdio.h>

int max(int x, int y){
    int result;
    if (x > y){
        result = x;
    }else{
        result = y;
    }
    
    return result;
}


int maxSubArray(int* nums, int numsSize){
    if (numsSize == 0){
        return 0;
    }

    int local_max_sum = nums[0];
    int global_max_sum = local_max_sum;

    for (int i=1;i<numsSize;i++){
        local_max_sum = nums[i]+local_max_sum>nums[i]?nums[i]+local_max_sum:nums[i];

        if(local_max_sum>global_max_sum){
            global_max_sum = local_max_sum;
        }
        printf("%d\n", local_max_sum);
    }
    
    return global_max_sum;
}

int main(){
    int nums[9] = {-2,1,-3,4,-1,2,1,-5,4};
    int numsSize = 9;
    int maxSum;

    maxSum = maxSubArray(nums, numsSize);
    printf("%d", maxSum);
}