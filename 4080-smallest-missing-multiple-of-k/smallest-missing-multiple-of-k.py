class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set(nums)
        multiplier = 1
        
        while True:
            current_multiple = k * multiplier
            if current_multiple not in seen:
                return current_multiple
            multiplier += 1
        