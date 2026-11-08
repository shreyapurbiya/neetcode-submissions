class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=0
        profit=0
        i = prices.index(buy)
        while i<len(prices):
            if prices[i]<buy:
                    buy = prices[i]
            if (prices[i]-buy)>profit:
                profit=prices[i]-buy
            i=i+1
        return profit
