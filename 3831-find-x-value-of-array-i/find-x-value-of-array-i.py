class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # dp[r] stores the number of subarrays ending at the 
        # previous position that have a product % k == r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # 1. Start a new single-element subarray
            new_dp[num_mod] += 1
            
            # 2. Extend existing subarrays from the previous step
            for r in range(k):
                if dp[r] > 0:
                    new_mod = (r * num_mod) % k
                    new_dp[new_mod] += dp[r]
            
            # Accumulate current step's subsegments into global answer
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp
            
        return ans