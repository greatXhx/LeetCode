class Solution:
    def maxSubArray(self, nums):
        """动态规划
        假设对于元素i，所有以它前面的元素结尾的子数组的长度都已经求得，那么以第i个元素结尾且和最大的连续子数组实际上         ，要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，要么是只包含第i个元素，
        即sum[i] = max(sum[i-1] + a[i], a[i])
        """
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax = nums[0]
        localMax = nums[0]
        for item in nums[1:]:
            if localMax > 0:
                localMax += item
            else:
                localMax = item
            if localMax>globalMax:
                globalMax = localMax

        return globalMax



if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray1(nums))