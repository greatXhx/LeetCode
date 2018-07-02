class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Write your code here
        if -10<x<10 :
            return x
        n1 = abs(x)               #都按正数进行操作
        b = str(n1)
        if len(b)>10:
            return 0
        b = b[::-1]
        result=int(b)
        if x<0:                   #判断是否要添加符号符号
            result=-result
        if -2147483648 < result < 2147483647:  #整数不溢出的条件
            return result
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    b = s.reverse(-654)
    print(b)