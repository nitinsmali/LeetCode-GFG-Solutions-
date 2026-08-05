class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        suspicious = [False] * n
        suspicious[k] = True
        queue = [k]

        for u in queue:
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]