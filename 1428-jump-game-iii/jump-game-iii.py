class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        seen = set()

        def jump(i):
            if i < 0 or i >= len(arr) or i in seen:
                return False
            if arr[i] == 0:
                return True

            seen.add(i)
            return jump(i+arr[i]) or jump(i-arr[i])

        return jump(start)