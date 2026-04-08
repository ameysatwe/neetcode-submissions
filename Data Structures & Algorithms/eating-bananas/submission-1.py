from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while True:
        #     tot = 0
        #     for pile in piles:
        #         tot += ceil(pile/speed)
            
        #     if tot <= h:
        #         return speed
        #     speed +=1
        

        # return speed


        l,r = 1,max(piles)
        res = r

        while l<=r:
            mid = (l+r)//2

            tot = 0
            for p in piles:
                tot += ceil(float(p)/mid)
            
            if tot <= h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        
        return res