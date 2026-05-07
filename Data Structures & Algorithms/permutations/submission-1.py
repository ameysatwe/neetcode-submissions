class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        used = [False] * len(nums)
        self.res = []
        self.bt([],nums,used)

        return self.res
    

    def bt(self,perm,nums,pick):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.bt(perm,nums,pick)
                perm.pop()
                pick[i] = False