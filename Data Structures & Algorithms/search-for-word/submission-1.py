class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])

        seen = set()


        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r<0 or r>= rows or c<0 or c>=cols or i>=len(word):
                return False
            if word[i]!=board[r][c]:
                return False
            if (r,c) in seen:
                return False
            
            
            seen.add((r,c))

            found = (
                dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            )

            seen.remove((r,c))

            return found
        

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False
        