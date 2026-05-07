class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap)>1:
            s1,s2 = -heapq.heappop(heap),-heapq.heappop(heap)

            if s1 == s2:
                continue
            else:
                val = abs(s2-s1)
                heapq.heappush(heap,-val)

        
        return -heap[0] if heap else 0
