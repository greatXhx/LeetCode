class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for x in range(1,n+1):
            result.append("Fizz"[x%3*4::]+"Buzz"[x%5*4::] or str(x))
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(3))