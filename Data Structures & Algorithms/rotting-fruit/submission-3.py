class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        # vis = set()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    # vis.add((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        
        time = 0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        while q and fresh>0:
            for _ in range(len(q)):
                (x,y) = q.popleft()
                for dx,dy in dirs:
                    i,j = x+dx,y+dy
                    if (0<=i<rows and 
                        0<=j<cols and
                        grid[i][j]==1):
                        grid[i][j] = 2
                        fresh-=1
                        q.append((i,j)) 
            time+=1

        return time if fresh==0 else -1


