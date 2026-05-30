class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        MAXX = 50001

        obstacles = [0, MAXX]

        size = 1
        while size < MAXX + 1 :
            size <<= 1
        seg = [0] * (2* size)

        def update(pos, val):
            pos += size
            seg[pos] = val
            pos //= 2
            
            while pos:
                seg[pos] = max(seg[2*pos], seg[2*pos+1])
                pos //= 2

        def query(l, r):
            l += size 
            r += size
            res = 0

            while l <= r:
                if l & 1:
                    res = max(rse, seg[1])
                    l += 1

                if not (r & 1):
                    res = max(res, seg[r])
                    r -= 1

                l //= 2
                r //= 2

            return res

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                idx = bisect_left(obstacles, x)
                left = obstacles[idx - 1]
                right = obstacles[idx]

                insort(obstacles, x)

                update(x, x - left)
                update(right, right - x)

            else:
                x, sz = q[1], q[2]

                idx = bisect_left(obstacles, x + 1)
                left = obstacles[idx - 1]
                best = query(0, x)
                best = max(best, x - left)
                ans.append(best >= sz)

        return ans
