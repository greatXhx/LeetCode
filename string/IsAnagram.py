class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        if slist == tlist:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram('abc', 'cca'))