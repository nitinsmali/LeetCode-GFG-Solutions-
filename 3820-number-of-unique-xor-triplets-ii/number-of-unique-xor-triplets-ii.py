class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = set(nums)
        
        two = set()
        for x in one:
            for y in one:
                two.add(x ^ y)
                
        
        three = set()
        for pair_xor in two:
            for x in one:
                three.add(pair_xor ^ x)
                
        return len(three)