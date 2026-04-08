class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # res = [[]]

        # for num in nums:

        #     res += [subset + [num] for subset in res]
        
        # return res

        res = []
        ss = []
        
        def dp(i):
            if i >= len(nums):
                res.append(ss[:])
                return
            ss.append(nums[i])
            dp(i+1)
            ss.pop()
            dp(i+1)
        
        dp(0)

        return res