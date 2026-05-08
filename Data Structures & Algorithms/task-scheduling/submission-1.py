class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskCount = Counter(tasks)
        ans = 0
        heap = []

        for task,val in taskCount.items():
            heapq.heappush(heap,(-val,task))
        

        while heap:
            temp = []
            cycle = n+1
            for _ in range(cycle):
                if heap:
                    count,task = heapq.heappop(heap)
                    if count+1 < 0:
                        temp.append((count+1,task))
                ans+=1
                if not heap and not temp:
                    break
    
    
            for item in temp:
                heapq.heappush(heap,item)
        
        return ans