class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        OFFSET = n + 1
        bit = [0] * (2 * n + 5)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        update(OFFSET, 1)
        
        prefix_sum = 0
        ans = 0
        
        for num in nums:
            if num == target:
                prefix_sum += 1
            else:
                prefix_sum -= 1
                
            ans += query(prefix_sum + OFFSET - 1)
            update(prefix_sum + OFFSET, 1)
            
        return ans
