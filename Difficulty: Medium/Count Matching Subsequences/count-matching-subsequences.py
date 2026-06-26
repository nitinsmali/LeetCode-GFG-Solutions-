class Solution:
    def countWays(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        MOD = 10**9 + 7
        
        dp = [0] * (m + 1)
        
        dp[0] = 1 
        
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = (dp[j] + dp[j - 1]) % MOD
                    
        return dp[m]