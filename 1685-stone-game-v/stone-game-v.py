class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """

        memo = {}

        def dfs(i, j):
            if i >= j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            ans = 0
            l = 0
            r = sum(stoneValue[i:j + 1])

            for k in range(i, j):
                l += stoneValue[k]
                r -= stoneValue[k]

                if l < r:
                    if ans >= l * 2:
                        continue

                    ans = max(ans, l + dfs(i, k))

                elif l > r:
                    if ans >= r * 2:
                        break

                    ans = max(ans, r + dfs(k + 1, j))

                else:
                    ans = max(
                        ans,
                        l + dfs(i, k),
                        r + dfs(k + 1, j)
                    )

            memo[(i, j)] = ans
            return ans

        return dfs(0, len(stoneValue) - 1)
        