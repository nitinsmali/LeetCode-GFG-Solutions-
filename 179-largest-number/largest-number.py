class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        rack = list(map(str, nums))

        def glow(a, b):
            if a + b > b + a:
                return -1

            elif a + b < b + a:
                return 1

        rack.sort(key=cmp_to_key(glow))

        ans = ''.join(rack)

        return '0' if ans[0] == '0' else ans