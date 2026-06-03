class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        
        def preprocess(start, dur):
            rides = sorted(zip(start, dur))

            s = [x for x, _ in rides]
            d = [y for _, y in rides]
            n = len(rides)

            pref = [0] * n          # min duration up to i
            pref[0] = d[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            suff = [0] * n          # min(start + duration) from i onward
            suff[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], s[i] + d[i])

            return s, pref, suff

        ws, wpref, wsuff = preprocess(waterStartTime, waterDuration)
        ls, lpref, lsuff = preprocess(landStartTime, landDuration)

        ans = float('inf')

        # Land -> Water
        for st, dur in zip(landStartTime, landDuration):
            t = st + dur
            k = bisect_right(ws, t)

            if k:
                ans = min(ans, t + wpref[k - 1])

            if k < len(ws):
                ans = min(ans, wsuff[k])

        # Water -> Land
        for st, dur in zip(waterStartTime, waterDuration):
            t = st + dur
            k = bisect_right(ls, t)

            if k:
                ans = min(ans, t + lpref[k - 1])

            if k < len(ls):
                ans = min(ans, lsuff[k])

        return ans