class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        ss = []

        def rec(i):
            if i>=len(nums):
                res.append(ss[:])
                return
            
            ss.append(nums[i])
            rec(i+1)
            ss.pop()
            rec(i+1)
        

        rec(0)

        return res