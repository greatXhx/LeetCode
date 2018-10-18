class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dayNums = len(prices)
        maxPro = 0
        nowPro = 0
        for i in range(1, dayNums):
            profit = prices[i] - prices[i-1]
            nowPro += profit
            if nowPro<0:
                nowPro = 0
            elif nowPro > maxPro:
                maxPro = nowPro
        return maxPro

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        maxPro = 0
        while i<len(prices)-1:
            if prices[i]<prices[i+1]:
                maxPro = maxPro+(prices[i+1]-prices[i])
            i=i+1
        return maxPro

    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dayNums = len(prices)
        globalMaxProfit = [0 for row in range(3)]
        localMaxProfit = [0 for row in range(3)]
        for i in range(1, dayNums):
            profit = prices[i] - prices[i-1]
            for j in range(2,0,-1):
                localMaxProfit[j] = max(globalMaxProfit[j-1] + max(0, profit), localMaxProfit[j]+profit)
                globalMaxProfit[j] = max(globalMaxProfit[j], localMaxProfit[j])
        return globalMaxProfit[2]

    def maxProfit4(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 当交易天数大于天数-1的时候，就变成了Best Time to Buy and Sell Stock II
        if k >= len(prices) // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)

        dayNums = len(prices)
        globalMaxProfit = [0 for row in range(k+1)]
        localMaxProfit = [0 for row in range(k+1)]
        for i in range(1, dayNums):
            profit = prices[i] - prices[i-1]
            for j in range(k,0,-1):
                localMaxProfit[j] = max(globalMaxProfit[j-1] + max(0, profit), localMaxProfit[j]+profit)
                globalMaxProfit[j] = max(globalMaxProfit[j], localMaxProfit[j])
        return globalMaxProfit[k]


if __name__ == "__main__":
    s = Solution()
    prices = [1,2,4,2,5,7,2,4,9,0]
    # prices = [7,1,5,3,6,4]
    print(s.maxProfit4(4, prices))