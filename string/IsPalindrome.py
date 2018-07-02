class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        result = ''.join(re.split('[^A-Za-z0-9]', s))
        s = result.lower()
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Abc123,sdf"))