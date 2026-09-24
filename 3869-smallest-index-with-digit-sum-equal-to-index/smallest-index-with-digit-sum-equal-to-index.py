class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
        # Calculate the sum of digits of abs(nums[i]) to handle any negative numbers
            digit_sum = sum(int(digit) for digit in str(abs(nums[i])))
            
            if digit_sum == i:
                return i
            
        return -1