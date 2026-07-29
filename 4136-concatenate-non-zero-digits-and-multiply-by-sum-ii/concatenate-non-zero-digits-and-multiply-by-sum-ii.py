class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        m = len(s)
        
        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # Initialize prefix arrays
        prefix_sum = [0] * (m + 1)
        prefix_nz_count = [0] * (m + 1)
        prefix_num = [0] * (m + 1)
        
        for i in range(m):
            digit = int(s[i])
            
            prefix_sum[i + 1] = prefix_sum[i] + digit
            
            if digit != 0:
                prefix_nz_count[i + 1] = prefix_nz_count[i] + 1
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD
            else:
                prefix_nz_count[i + 1] = prefix_nz_count[i]
                prefix_num[i + 1] = prefix_num[i]
                
        ans = []
        for l, r in queries:
            # 1. Calculate the sum of digits in the query range
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            
            # 2. Extract the non-zero concatenated integer x
            nz_in_range = prefix_nz_count[r + 1] - prefix_nz_count[l]
            
            if nz_in_range == 0:
                x = 0
            else:
                # Slicing out the range value using our precomputed powers of 10
                subtracted_part = (prefix_num[l] * pow10[nz_in_range]) % MOD
                x = (prefix_num[r + 1] - subtracted_part + MOD) % MOD
                
            # 3. Compute (x * sum) % MOD
            ans.append((x * digit_sum) % MOD)
            
        return ans
        