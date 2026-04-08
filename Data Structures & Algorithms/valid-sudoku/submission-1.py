class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sq = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                    
                if curr in rows[r] or curr in cols[c] or curr in sq[(r//3,c//3)]:
                    return False
                
                rows[r].add(curr)
                cols[c].add(curr)
                sq[(r//3,c//3)].add(curr)

        return True