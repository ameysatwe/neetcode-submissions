class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])

        q = deque()

        vis = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    vis.add((i,j))
        

        dist = 0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            for _ in range(len(q)):
                (x,y) = q.popleft()
                grid[x][y] = dist
                for dx,dy in dirs:
                    r,c = x+dx,y+dy
                    if r>=0 and r<rows and c>=0 and c<cols and (r,c) not in vis:
                        if grid[r][c]!=-1:
                            q.append((r,c))
                            vis.add((r,c))

            dist+=1 