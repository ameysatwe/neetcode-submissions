class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def rec(i):
            if i>=len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i]=max(nums[i]+rec(i+2),rec(i+1))
            return memo[i]
        
        return rec(0)