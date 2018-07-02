class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        dic=collections.Counter(s)#使用字典key:s, value:s中元素出现的次数
        print(dic)
        for i in range(len(s)):
            if dic[s[i]]==1:#如果字典中value为1
                return i
        return -1



if __name__ == "__main__":
    a = 'abcca'
    s = Solution()
    b = s.firstUniqChar(a)
    print(b)