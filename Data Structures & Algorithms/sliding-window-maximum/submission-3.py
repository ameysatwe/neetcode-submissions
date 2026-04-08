class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # for i in range(len(nums)-k+1):
        #     res.append(
        #         max(nums[i:i+k])
        #     )
            
        # return res

        hp = []
        op = []

        for i in range(len(nums)):
            heapq.heappush(hp,(-nums[i],i))
            if i>=k-1:
                while hp[0][1] <= i-k:
                    heapq.heappop(hp)
                op.append(-hp[0][0])
        
        return op