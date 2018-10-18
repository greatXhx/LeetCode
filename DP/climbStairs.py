"""
动态规划来解决。关键是找出递推式。
到第十阶，那么我到第十阶的方法可以是第九阶上一步，或者第八阶上两步
那么我第十阶的方法就有，第九阶+第八阶了
同理，如果可以一次3阶，
那么我们的递归，不就是变成前三个数了

"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stepNumber=[]
        stepNumber.append(1)
        stepNumber.append(2)
        for i in range(2, n):
            stepNumber.append(stepNumber[i-1]+stepNumber[i-2])
        return stepNumber[n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(5))