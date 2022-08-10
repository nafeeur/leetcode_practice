class Solution:
          
    maxGoldFound = 0
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dfs(grid, i, j, 0)
        return self.maxGoldFound

    def dfs(self, grid, i, j, currGold):
        width, height = len(grid[0]), len(grid)
        if i < 0 or j < 0 or i >= height or j >= width or grid[i][j] == 0:
            return
        goldInCell = grid[i][j]
        totalGold = currGold + goldInCell
        if totalGold > self.maxGoldFound:
            self.maxGoldFound = totalGold
        grid[i][j] = 0
        self.dfs(grid, i - 1, j, totalGold)
        self.dfs(grid, i + 1, j, totalGold)
        self.dfs(grid, i, j + 1, totalGold)
        self.dfs(grid, i, j - 1, totalGold)
        grid[i][j] = goldInCell
            
    
                    
        