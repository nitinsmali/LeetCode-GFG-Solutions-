class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        
        # suffix_sum[i] stores the total stones from pile i to the end
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, M):
            # Base case: If the current player can take all remaining piles
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            # Find the option that minimizes the opponent's maximum score
            max_stones = 0
            for x in range(1, 2 * M + 1):
                opponent_score = dp(i + x, max(M, x))
                current_score = suffix_sum[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            memo[(i, M)] = max_stones
            return max_stones
        
        return dp(0, 1)
        