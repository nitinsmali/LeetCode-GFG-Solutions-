class Solution:
    def findCoverage(self, matrix):
        n, m = len(matrix), len(matrix[0])
        total_coverage = 0
        
        # 1. Left-to-Right & Right-to-Left Row Checks
        for r in range(n):
            has_seen_one = False
            for c in range(m):
                if matrix[r][c] == 1: has_seen_one = True
                elif matrix[r][c] == 0 and has_seen_one: total_coverage += 1
                
            has_seen_one = False
            for c in range(m - 1, -1, -1):
                if matrix[r][c] == 1: has_seen_one = True
                elif matrix[r][c] == 0 and has_seen_one: total_coverage += 1
                
        # 2. Top-to-Bottom & Bottom-to-Top Column Checks
        for c in range(m):
            has_seen_one = False
            for r in range(n):
                if matrix[r][c] == 1: has_seen_one = True
                elif matrix[r][c] == 0 and has_seen_one: total_coverage += 1
                
            has_seen_one = False
            for r in range(n - 1, -1, -1):
                if matrix[r][c] == 1: has_seen_one = True
                elif matrix[r][c] == 0 and has_seen_one: total_coverage += 1
                
        return total_coverage
