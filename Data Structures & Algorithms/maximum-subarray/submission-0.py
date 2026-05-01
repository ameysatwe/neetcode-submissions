class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ms = -1

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                s = sum(nums[i:j+1])
                ms = max(s,ms)
        
        return ms