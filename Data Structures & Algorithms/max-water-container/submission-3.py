class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0

        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         curr = min(heights[i],heights[j])*(j-i)
        #         area = max(area,curr)
        # return area 

        l,r = 0,len(heights)-1

        while l<=r:
            area = max(min(heights[l],heights[r])*(r-l),area)
            # res = 
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        
        return area