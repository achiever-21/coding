. Count Submatrices with Top-Left Element and Sum Less Than k
-----------------------------#################-------------------------------
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row=len(grid)
        col=len(grid[0])
        haha=0
        for i in range(row):
            for j in range(col):
                if i>0:
                    grid[i][j]+=grid[i-1][j]
                if j>0:
                    grid[i][j]+=grid[i][j-1]
                if i>0 and j>0:
                    grid[i][j]-=grid[i-1][j-1]
                if grid[i][j]<=k:
                    haha+=1
                else:
                    break
        return haha
--------------------------
