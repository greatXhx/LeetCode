class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        temp = [0]*n
        count = 0
        for i in range(2,n):
            if temp[i] == 0:
                count+=1
                for j in range(i, n, i):
                    temp[j] = 1
                #temp[i] = 0
        return count
if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(15))

