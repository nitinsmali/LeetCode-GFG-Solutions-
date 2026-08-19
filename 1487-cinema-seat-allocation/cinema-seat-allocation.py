class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved_in_rows = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_in_rows[row] |= (1 << (seat - 2))
                
        max_groups = 2 * (n - len(reserved_in_rows))
        
        left_mask = 0b00001111   # seats 2,3,4,5
        right_mask = 0b11110000  # seats 6,7,8,9
        mid_mask = 0b00111100    # seats 4,5,6,7
        
        for mask in reserved_in_rows.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            mid_free = (mask & mid_mask) == 0
            
            if left_free and right_free:
                max_groups += 2
            elif left_free or right_free or mid_free:
                max_groups += 1
                
        return max_groups