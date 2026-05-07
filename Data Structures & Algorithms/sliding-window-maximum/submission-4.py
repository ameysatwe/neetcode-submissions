class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = [0]*(len(nums)-k+1)

        # window = nums[0:k]

        # res[0] = max(window)

        for i in range(len(nums)-k+1):
            res[i] = max(nums[i:i+k])
        
        return res

        