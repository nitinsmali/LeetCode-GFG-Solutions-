class Solution:
    def largestArea(self, n, m, arr):
        # code here
        rows = [0, n + 1]
        cols = [0, m + 1]
        
        for r, c in arr:
            rows.append(r)
            cols.append(c)
            
        rows.sort()
        cols.sort()
        
        max_r = 0
        for i in range(1, len(rows)):
            max_r = max(max_r, rows[i] - rows[i-1] - 1)
            
        max_c = 0
        for j in range(1, len(cols)):
            max_c = max(max_c, cols[j] - cols[j-1] - 1)
            
        return max_r * max_c