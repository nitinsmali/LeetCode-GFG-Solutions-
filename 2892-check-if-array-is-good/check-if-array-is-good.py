class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        peak = max(nums)

        if len(nums) != peak +1:
            return False

        bag = [0] * (peak + 1)

        for x in nums:
            if x > peak or x < 1:
                return False
            bag[x] +=1

        for y in range(1, peak):
            if bag[y] != 1:
                return False
        return bag[peak] ==2