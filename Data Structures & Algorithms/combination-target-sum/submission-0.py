class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        ss = []

        def dp(i,curr,total):
            if total == target:
                res.append(curr[:])
                return
            
            if i>= len(nums) or total>target:
                return
            
            curr.append(nums[i])
            dp(i,curr,total+nums[i])
            curr.pop()
            dp(i+1,curr,total)

        

        dp(0,[],0)
        return res