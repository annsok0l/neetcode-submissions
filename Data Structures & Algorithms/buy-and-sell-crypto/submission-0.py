class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        start = 0

        for end in range (1,len(prices)):
            if prices[end]>min_price:
                profit = prices[end]- prices[start]
                max_profit = max(profit, max_profit)
                end +=1
            elif prices[end]<min_price:
                min_price = prices[end]
                start = end
            
        return max_profit

        