class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []

        for i,h in enumerate(heights):
            st =i

            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                st = index
            stack.append((st,h))
        

        for i,h in stack:
            maxArea = max(maxArea,h * (len(heights)-i))
        
        return maxArea