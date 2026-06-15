class Solution:
    def minimumCost(self, cost: list[int], w: int) -> int:
        # dp[j] will store the minimum cost to buy exactly j kg
        dp = [float('inf')] * (w + 1)
        dp[0] = 0  # 0 kg costs 0
        
        # Loop through each available packet weight (1-indexed based on position)
        for i in range(len(cost)):
            # Skip if the packet size is not available (-1)
            if cost[i] == -1:
                continue
                
            packet_weight = i + 1
            packet_cost = cost[i]
            
            # Update dp array for all weights from packet_weight up to w
            for j in range(packet_weight, w + 1):
                if dp[j - packet_weight] != float('inf'):
                    dp[j] = min(dp[j], dp[j - packet_weight] + packet_cost)
                    
        # If dp[w] is still infinity, it's impossible to make exactly w kg
        return dp[w] if dp[w] != float('inf') else -1
