class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        将单位阵一圈一圈的旋转，共置换n/2圈
        每圈内循环n-1次，每次四个对应位置旋转
        旋转完一行旋转次数加1
        思路参考https://blog.csdn.net/sweeterer/article/details/52217230
        """
        temp = 0
        length = len(matrix[0])
        count = 0    ##记录已经旋转的圈数的次数
        for i in range(int(length/2)):   ## 一共进行
             for j in range(length-1, 0, -1):
                temp = matrix[0+count][j+count]
                matrix[0+count][j+count] = matrix[length-1-j+count][0+count]
                matrix[length - 1 - j +count][0+count] = matrix[length-1+count][length-1-j+count]
                matrix[length - 1 + count][length - 1 - j+count] = matrix[j+count][length - 1 + count]
                matrix[j+count][length - 1 + count] = temp
             length = length - 2
             count = count+1


if __name__ =="__main__":
    a = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ]
    b = [
             [5,1,9,11],
             [2,4,8,10],
             [13,3,6,7],
             [15,14,12,16]
         ]
    print(b)
    s = Solution()
    s.rotate(b)
    print(b)
