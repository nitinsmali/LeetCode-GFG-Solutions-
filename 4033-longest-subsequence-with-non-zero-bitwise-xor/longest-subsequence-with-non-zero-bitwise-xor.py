class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = functools.reduce(lambda x, y: x ^ y, nums, 0)
        
        if total_xor != 0:
            return len(nums)
            
        return len(nums) - 1 if any(x != 0 for x in nums) else 0
        