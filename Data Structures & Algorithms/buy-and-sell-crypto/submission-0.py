class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp,maxp = prices[0],0

        for i in prices:
            maxp = max(maxp,i-minp)
            minp = min(minp,i)

        
        return maxp