class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        
        # row = len(grid), collumn = len(grid[0])
        # max_output = 0, 2 for loops, dfs helper function
        # grid[i][j] = 0
        
        
        r = len(grid)
        c = len(grid[0])
        max_out = 0
        def dfs(i,j):
            if(i >= r or j >= c or i < 0 or j < 0 or grid[i][j] == 0):
                return 0
            
            curr = grid[i][j]
            grid[i][j] = 0
            right = dfs(i, j+1)
            left = dfs(i, j-1)
            top = dfs(i-1, j)
            down = dfs(i+1, j)
            out = max(right,left,top,down) + curr
            grid[i][j] = curr
            
            return out
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    max_out = max(dfs(i,j), max_out)
        
      
        return max_out
            
    
                    
        