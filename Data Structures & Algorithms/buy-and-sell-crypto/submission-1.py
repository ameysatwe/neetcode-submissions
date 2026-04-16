class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp,maxp = prices[0],0

        for price in prices:
            minp = min(minp,price)
            maxp = max(maxp,price - minp)

        return maxp