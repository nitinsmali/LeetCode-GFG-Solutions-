class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        buy_separate = (need1 * cost1) + (need2 * cost2)
        
        # Option 2: Buy only combo items (covers the larger requirement)
        buy_all_both = max(need1, need2) * costBoth
        
        # Option 3: Buy combo items for the overlapping need, then buy the rest individually
        common = min(need1, need2)
        buy_mixed = (common * costBoth) + ((need1 - common) * cost1) + ((need2 - common) * cost2)
        
        return min(buy_separate, buy_all_both, buy_mixed)