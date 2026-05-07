class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def rec(i):
            if i>=len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            rec(i+1)
            subset.pop()
            rec(i+1)
        
        rec(0)

        return res