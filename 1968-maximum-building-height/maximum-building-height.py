class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])
        restrictions.sort()
        
        m = len(restrictions)
        
        # Forward Pass
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + (restrictions[i][0] - restrictions[i-1][0]))
            
        # Backward Pass
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))
            
        # Calculate the maximum possible peak height
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        # Account for the trailing buildings up to building n
        if restrictions[-1][0] < n:
            max_height = max(max_height, restrictions[-1][1] + (n - restrictions[-1][0]))
            
        return max_height
            
