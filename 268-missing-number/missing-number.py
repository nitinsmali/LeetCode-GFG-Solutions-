class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        a = n*(n+1)//2
        b = sum(nums)
        
        return a - b