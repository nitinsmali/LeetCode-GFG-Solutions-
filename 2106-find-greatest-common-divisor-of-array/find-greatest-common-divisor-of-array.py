class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)
        
        # Custom Euclidean algorithm for GCD
        while max_num:
            min_num, max_num = max_num, min_num % max_num
            
        return min_num
