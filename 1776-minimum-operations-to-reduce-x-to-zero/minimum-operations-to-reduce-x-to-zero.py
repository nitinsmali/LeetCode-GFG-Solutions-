class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target, max_len, current_sum, left = sum(nums) - x, -1, 0, 0
        if target < 0: return -1
        if target == 0: return len(nums)

        for right, val in enumerate(nums):
            current_sum += val
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1