class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        queue = deque([0])
        visited = {0}
        steps = 0

        while queue :
            for _ in range(len(queue)):
                i = queue.popleft()

                if i == n - 1:
                    return steps


                neighbors = []

                neighbors.extend(graph[arr[i]])

                if i + 1 < n:
                    neighbors.append(i + 1)

                if i - 1 >= 0:
                    neighbors.append(i - 1)

                for nei in neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

                graph[arr[i]]=[]

            steps += 1

        return -1