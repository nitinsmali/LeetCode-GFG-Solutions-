class Solution:
    def minOperations(self, b: list[int]) -> int:
        # Import inside the method to prevent evaluation environment NameErrors
        import math
        
        n = len(b)
        visited = [False] * (n + 1)
        MOD = 10**9 + 7
        ans = 1
        
        # 1-based indexing map adjustment
        b_1indexed = [0] + b
        
        for i in range(1, n + 1):
            if not visited[i]:
                cycle_length = 0
                curr = i
                
                while not visited[curr]:
                    visited[curr] = True
                    curr = b_1indexed[curr]
                    cycle_length += 1
                
                ans = (ans * cycle_length) // math.gcd(ans, cycle_length)
                
        return ans % MOD
