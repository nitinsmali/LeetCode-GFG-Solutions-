class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        seen = []
        k = 0
        
        for x in nums:
            if x == -1:
                k += 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k - 1])
            else:
                k = 0
                seen.insert(0, x)
                
        return ans

        