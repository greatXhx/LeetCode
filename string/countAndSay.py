def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    output = '1'
    for i in range(n-1):
        j = 0
        count = 0
        output1 = ''
        while(j<len(output)):
            while j<len(output)-1 and output[j] == output[j+1] :
                j = j+1
                count = count+1
            output1 = output1 + str(count+1) + str(output[j])
            count = 0
            j = j+1

        output = output1
    return output

if __name__ == "__main__":
    input = 6
    print(countAndSay(input))