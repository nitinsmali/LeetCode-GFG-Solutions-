class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        memo = set()
        
        def dfs(i: int, j: int, k: int) -> bool:
            if i >= m or j >= n or k < 0:
                return False
                
            k += 1 if grid[i][j] == '(' else -1
            
            if k < 0:
                return False
                
            remaining_steps = (m - 1 - i) + (n - 1 - j)
            if k > remaining_steps:
                return False
                
            if i == m - 1 and j == n - 1:
                return k == 0
                
            state = (i, j, k)
            if state in memo:
                return False
                
            if dfs(i + 1, j, k) or dfs(i, j + 1, k):
                return True
                
            memo.add(state)
            return False

        return dfs(0, 0, 0)