class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ans = float('inf')

        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))

        return ans
        