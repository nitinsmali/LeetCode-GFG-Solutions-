class Solution:
    def exitPoint(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        r, c, dir_idx = 0, 0, 0
        
        while True:
            if mat[r][c] == 1:
                mat[r][c] = 0
                dir_idx = (dir_idx + 1) % 4
                
            # Peek at the next step
            next_r = r + dr[dir_idx]
            next_c = c + dc[dir_idx]
            
            # If the next step is outside, the current cell is the exit point
            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                return [r, c]
                
            # Otherwise, move forward
            r, c = next_r, next_c
            