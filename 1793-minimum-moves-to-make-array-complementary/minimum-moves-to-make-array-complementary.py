class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        rail = [0] * (2 * limit + 2)

        n = len(nums)

        for i in range(n//2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit

            total = a+b

            rail[2] +=2
            rail[low] -= 1
            rail[total] -= 1
            rail[total +1] += 1
            rail[high +1] += 1

        best = float('inf')
        now = 0
        for s in range(2, 2*limit + 1):
            now += rail[s]
            best = min(best, now)

        return best