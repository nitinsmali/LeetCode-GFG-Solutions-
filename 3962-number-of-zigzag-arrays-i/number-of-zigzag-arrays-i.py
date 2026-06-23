class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        V = r - l + 1
        
        # Base cases for length 2
        dp_up = [v for v in range(V)]
        dp_down = [(V - 1 - v) for v in range(V)]
        
        # Build states up to length n
        for i in range(3, n + 1):
            next_up = [0] * V
            next_down = [0] * V
            
            # Compute next_up using prefix sum of dp_down
            pref_down = 0
            for v in range(V):
                next_up[v] = pref_down % MOD
                pref_down += dp_down[v]
                
            # Compute next_down using suffix sum of dp_up
            suff_up = 0
            for v in range(V - 1, -1, -1):
                next_down[v] = suff_up % MOD
                suff_up += dp_up[v]
                
            dp_up = next_up
            dp_down = next_down
            
        return (sum(dp_up) + sum(dp_down)) % MOD

                    