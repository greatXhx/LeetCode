class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        contend = re.findall(r"^[-+]?\d+", str.strip())##r'' 使r中的字符串失去转义
        if contend:
            contend = contend[0]
            print(contend)
            if contend[0] == "-" or contend[0] == "+":
                contend1 = contend[1:]
                str_int = int(contend1)
            else:
                str_int = int(contend)

            if contend[0] == "-":
                return -str_int if str_int <= 2**31 else -2**31
            else:
                return str_int if str_int < 2**31 else 2**31-1
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    input = '42'
    print(s.myAtoi(input))