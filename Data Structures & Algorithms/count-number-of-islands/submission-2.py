class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        vis = set()
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == "0":
                return
            
            # if (r,c) in vis:
            #     return

            grid[r][c] = "0"
            
            # if grid[r][c] == "1":
            #     return True
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        num_islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    num_islands+=1
        
        return num_islands