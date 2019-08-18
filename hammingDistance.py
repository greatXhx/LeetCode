class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dis = 0
        for i in range(32):
            if (x &(1<<i))^(y&1<<i):
                dis+=1

        return dis

if __name__ == "__main__":
    s = Solution()
    a = 0b0101001
    b = 0b0101010
    print(s.hammingDistance(a,b))
