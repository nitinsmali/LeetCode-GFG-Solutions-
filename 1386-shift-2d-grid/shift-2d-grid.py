class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k = k % total
        
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                new_flat = (r * n + c + k) % total
                new_r = new_flat // n
                new_c = new_flat % n
                res[new_r][new_c] = grid[r][c]
                
        return res