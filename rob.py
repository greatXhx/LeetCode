class Solution:
    def rob(self, nums):

        """
        动态规划，当前的最大值取决于 到前一户的最大值 和 到前两户的最大值加上当户的钱数
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:#一天都没有
            return 0
        maxMonney = [0,nums[0],nums[0]]#注意只有一天的情况
        for num in nums[1:]:
            maxMonney[2] = max(maxMonney[1], maxMonney[0]+num)
            maxMonney[0] = maxMonney[1]
            maxMonney[1] = maxMonney[2]
        return maxMonney[2]

if __name__ == "__main__":
    s = Solution()
    nums = [1]
    print(s.rob(nums))