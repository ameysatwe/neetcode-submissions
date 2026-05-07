class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def rec(i,curr,total):
            if total == target:
                res.append(curr[:])
                return
            
            if i>=len(nums) or total > target:
                return
            
            curr.append(nums[i])
            rec(i,curr,total+nums[i])
            curr.pop()
            rec(i+1,curr,total)
        
        rec(0,[],0)

        return res