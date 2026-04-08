class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []

        c = Counter(nums)

        for n,v in c.items():
            heapq.heappush(pq,(v,n))

            while len(pq) > k:
                heapq.heappop(pq)
        

        return [x[1] for x in pq]
        
        