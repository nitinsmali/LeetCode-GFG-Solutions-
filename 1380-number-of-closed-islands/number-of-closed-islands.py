class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 0:
                grid[r][c] = 1
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(R):
            for c in range(C):
                if (r == 0 or r == R - 1 or c == 0 or c == C - 1) and grid[r][c] == 0:
                    dfs(r, c)
                    
        ans = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if grid[r][c] == 0:
                    ans += 1
                    dfs(r, c)
                    
        return ans