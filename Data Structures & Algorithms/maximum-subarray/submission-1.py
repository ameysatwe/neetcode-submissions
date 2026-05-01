class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ms ,curr = nums[0],0

        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         s = sum(nums[i:j+1])
        #         ms = max(s,ms)
        
        # return ms

        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            ms = max(ms,curr)

        return ms
            
