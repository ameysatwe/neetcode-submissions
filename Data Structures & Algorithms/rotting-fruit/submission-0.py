class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        # vis = set()
        q = deque()
        self.fresh = 0

        def addOrange(r,c):
            if r<0 or r==rows or c<0 or c==cols:
                return
            if grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append((r,c))
            self.fresh-=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        
        time = 0

        while q and self.fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()

                addOrange(r+1,c)
                addOrange(r-1,c)
                addOrange(r,c+1)
                addOrange(r,c-1)

            

            time+=1

        return time if self.fresh == 0 else -1

            