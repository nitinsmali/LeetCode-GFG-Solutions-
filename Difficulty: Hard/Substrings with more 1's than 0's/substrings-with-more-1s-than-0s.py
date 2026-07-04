class Solution:
    def countSubstring(self, s):
        # code here
        n = len(s)
        tree_size = 2 * n + 2
        bit = [0] * tree_size
        
        def update(idx: int, val: int):
            while idx < tree_size:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total

        offset = n + 1
        update(0 + offset, 1)
        
        current_sum = 0
        ans = 0
        
        for char in s:
            current_sum += 1 if char == '1' else -1
            ans += query(current_sum + offset - 1)
            update(current_sum + offset, 1)
            
        return ans
