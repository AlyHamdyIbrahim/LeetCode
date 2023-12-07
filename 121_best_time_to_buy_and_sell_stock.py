class Solution:
    def maxProfit(self, prices: [int]) -> int:
        cheapestPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if price < cheapestPrice:
                cheapestPrice = price
            else:
                maxProfit = max(maxProfit, price - cheapestPrice)
        
        return maxProfit