class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        # queue = deque()

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1

        queue = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for child in graph[node]:
                indegree[child]-=1
                if indegree[child] == 0:
                    queue.append(child)

        
        if len(res)!=numCourses:
            return []
        
        return res[::-1]
