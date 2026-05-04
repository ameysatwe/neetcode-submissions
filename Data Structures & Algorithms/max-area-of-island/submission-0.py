class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        vis = set()


        def dfs(r,c):
            if r<0 or r>=rows:
                return 0
            
            if c<0 or c>=cols:
                return 0
            
            if grid[r][c] ==0:
                return 0
            
            if (r,c) in vis:
                return 0
            

            vis.add((r,c))


            return (1 + dfs(r-1,c) + dfs(r+1,c)+ dfs(r,c-1)+dfs(r,c+1))
        

        area = 0
        for i in range(rows):
            for j in range(cols):
                
                area = max(area,dfs(i,j))
        
        return area