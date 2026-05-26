class Solution:
    def topKFrequent(self, nums: List[int], l: int) -> List[int]:
        cnt = Counter(nums)

        min_heap = []

        for k,v in cnt.items():
            heapq.heappush(min_heap,(v,k))
            while len(min_heap)>l:
                heapq.heappop(min_heap)
        
        return [v for _,v in min_heap]