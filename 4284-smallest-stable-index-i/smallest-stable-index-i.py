class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
            
        # Step 1: Build max_left array
        max_left = [0] * n
        current_max = nums[0]
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            max_left[i] = current_max
            
        # Step 2: Build min_right array
        min_right = [0] * n
        current_min = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            min_right[i] = current_min
            
        # Step 3: Find the first index where instability <= k
        for i in range(n):
            instability_score = max_left[i] - min_right[i]
            if instability_score <= k:
                return i
                
        return -1