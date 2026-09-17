class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sums = {0: -1}
        current_sum = 0
        n = len(arr)
        
        # min_len[i] stores the minimum length of a valid sub-array found in arr[0...i]
        min_len = [float('inf')] * n
        
        ans = float('inf')
        best_till_now = float('inf')
        
        for i, num in enumerate(arr):
            current_sum += num
            
            # Check if there is a prefix sum such that current_sum - prefix_sum = target
            if current_sum - target in prefix_sums:
                start_idx = prefix_sums[current_sum - target]
                current_len = i - start_idx
                
                # Update the global minimum if a valid non-overlapping sub-array exists before start_idx
                if start_idx >= 0 and min_len[start_idx] != float('inf'):
                    ans = min(ans, current_len + min_len[start_idx])
                    
                best_till_now = min(best_till_now, current_len)
                
            min_len[i] = best_till_now
            prefix_sums[current_sum] = i
            
        return ans if ans != float('inf') else -1