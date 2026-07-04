class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))
        
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            for neighbor, dist in adj[node]:
                min_score = min(min_score, dist)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
        