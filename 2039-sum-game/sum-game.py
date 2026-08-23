class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        mid = n // 2
        
        # Split into first and second halves
        first_half = num[:mid]
        second_half = num[mid:]
        
        # Calculate known sums
        s1 = sum(int(c) for c in first_half if c != '?')
        s2 = sum(int(c) for c in second_half if c != '?')
        
        # Count question marks
        q1 = first_half.count('?')
        q2 = second_half.count('?')
        
        # If the mathematical equation holds, Bob wins (returns False)
        # Rearranged to avoid floating-point division
        if 2 * (s1 - s2) == 9 * (q2 - q1):
            return False
            
        return True