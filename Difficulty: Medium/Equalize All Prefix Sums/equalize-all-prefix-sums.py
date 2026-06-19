class Solution:
    def optimalArray(self, arr : list[int]) -> list[int]:
        n = len(arr)
        ans = []
        
        pref_sum = [0] * n
        current_sum = 0
        for i in range(n):
            current_sum += arr[i]
            pref_sum[i] = current_sum
            
        def get_range_sum(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == 0:
                return pref_sum[right]
            return pref_sum[right] - pref_sum[left - 1]

        for i in range(n):
            m = i // 2  
            median_val = arr[m]
            
            left_count = m + 1
            left_sum = get_range_sum(0, m)
            left_ops = (left_count * median_val) - left_sum
            
            right_count = i - m
            right_sum = get_range_sum(m + 1, i)
            right_ops = right_sum - (right_count * median_val)
            
            ans.append(left_ops + right_ops)
            
        return ans
