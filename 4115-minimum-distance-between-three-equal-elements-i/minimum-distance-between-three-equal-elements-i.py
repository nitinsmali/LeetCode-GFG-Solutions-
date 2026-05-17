class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float('inf')

        for indices in pos.values():

            # need at least 3 occurrences
            if len(indices) < 3:
                continue

            # check consecutive triples
            for i in range(len(indices) - 2):
                a = indices[i]
                b = indices[i + 1]
                c = indices[i + 2]

                dist = abs(a - b) + abs(b - c) + abs(c - a)

                ans = min(ans, dist)

        return ans if ans != float('inf') else -1
        