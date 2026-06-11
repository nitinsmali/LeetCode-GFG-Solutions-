class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Use BFS to find the maximum depth from root 1
        max_depth = 0
        queue = deque([(1, 0)]) # (node, current_depth)
        visited = {1}
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
        # Step 3: Compute 2^(max_depth - 1) % MOD
        return pow(2, max_depth - 1, MOD)