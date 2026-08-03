class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        # Indented 8 spaces to sit inside the method
        dp = [0] * (n + 3) 
        
        # Fill the DP array from right to left
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp[i + 1]
            
            take2 = float('-inf')
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                
            take3 = float('-inf')
            if i + 2 < n:
                take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                
            dp[i] = max(take1, take2, take3)
            
        # Evaluates the first stone to determine game outcome
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
