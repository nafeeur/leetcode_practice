class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_Islands = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(grid, r, c):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == '1':
                grid[r][c] = '0'
                
                for row, col in directions:
                    dfs(grid, r+row, c+col)
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num_of_Islands += 1
                    dfs(grid, r, c)
        return num_of_Islands