class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        area = -1

        while l<r:
            curr = min(heights[r],heights[l]) * (r-l)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1

            area = max(curr,area)

        return area