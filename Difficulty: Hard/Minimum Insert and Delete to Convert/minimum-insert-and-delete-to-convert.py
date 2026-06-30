from bisect import bisect_left

class Solution:
    def minInsAndDel(self, a, b):
        n = len(a)
        m = len(b)

        # Map value -> index in b
        pos = {value: i for i, value in enumerate(b)}

        # Convert common elements of a into indices of b
        arr = []
        for x in a:
            if x in pos:
                arr.append(pos[x])

        # Find LIS of indices
        lis = []
        for x in arr:
            i = bisect_left(lis, x)
            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x

        lcs = len(lis)

        return (n - lcs) + (m - lcs)