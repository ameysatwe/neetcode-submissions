class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix),len(matrix[0])
        lo = 0
        hi = rows*cols-1

        while lo<=hi:
            mid = lo+ (hi - lo )//2
            row , col = mid//cols, mid%cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                hi = mid-1
            else:
                lo = mid+1
        
        return False
