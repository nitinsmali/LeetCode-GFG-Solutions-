class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count0 = sum(1 for x in stones if x % 3 == 0)
        count1 = sum(1 for x in stones if x % 3 == 1)
        count2 = sum(1 for x in stones if x % 3 == 2)
        
        # Case 1: Even number of 0-remainder stones
        if count0 % 2 == 0:
            return count1 > 0 and count2 > 0
        
        # Case 2: Odd number of 0-remainder stones
        return abs(count1 - count2) > 2
        