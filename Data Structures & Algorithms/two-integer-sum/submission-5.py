class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        
        
        # return [0,0]

        complements = {}

        for i,v in enumerate(nums):
            if target - v in complements:
                return [complements[target-v],i]
            else:
                complements[v] = i
        