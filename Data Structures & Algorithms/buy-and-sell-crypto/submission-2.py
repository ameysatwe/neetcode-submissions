class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = -1
        min_p = float('inf')
        for p in prices:
            min_p = min(p,min_p)
            mp = max(mp,p-min_p)
        
        return mp