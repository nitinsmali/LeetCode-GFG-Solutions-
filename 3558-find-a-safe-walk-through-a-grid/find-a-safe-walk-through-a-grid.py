class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        dist = [[float('inf')] * n for _ in range(m)]
        
        start_cost = grid[0][0]
        dist[0][0] = start_cost
        
        dq = deque([(start_cost, 0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while dq:
            cost, r, c = dq.popleft()
            
            if cost > dist[r][c]:
                continue
                
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]
                    
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        
                        if grid[nr][nc] == 0:
                            dq.appendleft((new_cost, nr, nc))
                        else:
                            dq.append((new_cost, nr, nc))
                            
        return health - dist[m - 1][n - 1] >= 1
