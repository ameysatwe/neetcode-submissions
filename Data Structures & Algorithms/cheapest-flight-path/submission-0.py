class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for _ in range(n)]
        dist = [[float('inf')]*(k+5) for _ in range(n)]

        for u,v,cost in flights:
            adj[u].append([v,cost])

        dist[src][0] = 0
        minHeap = [(0,src,-1)] #cost,node,stops

        while minHeap:
            cost,node,stops = heapq.heappop(minHeap)
            if dst == node: return cost
            if stops == k or dist[node][stops+1] < cost:
                continue
            
            for nei,w in adj[node]:
                nextCost = cost+w
                nextStops = 1+stops
                if dist[nei][nextStops+1] > nextCost:
                    dist[nei][nextStops+1] = nextCost
                    heapq.heappush(minHeap,(nextCost,nei,nextStops))
            
        return -1