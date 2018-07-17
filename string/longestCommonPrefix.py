def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        minSubStr = strs[0]
        length = len(strs[0])
        for subStr in strs:
            length = len(subStr) if len(subStr)<length else length
        index = 0
        if not length:
            return ""
        while(index<length):
            for subStr in strs:
                if subStr[index] != minSubStr[index]:
                    return minSubStr[:index]
            index = index+1
        return minSubStr[:length]

def longestCommonPrefixBestsummit(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest=min(strs,key=len)
    for x, y in enumerate(shortest):
        for s in strs:
            if s[x]!=y:
                return shortest[:x]
    return shortest


if __name__ =="__main__":
    input1 = ["flower", "flow", "flight"]
    input2 = ["dog","racecar","car"]
    input3 = ["cc", "c"]
    print(longestCommonPrefixBestsummit(input1))