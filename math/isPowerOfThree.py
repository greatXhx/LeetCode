class Solution:
    def isPowerOfThree(self, n):
        """
        而3在32位里最大为1162261467(3的19次方),所以用1162261467去除n取余
        :type n: int
        :rtype: bool
        """
        return n>0 and (1162261467%n==0)