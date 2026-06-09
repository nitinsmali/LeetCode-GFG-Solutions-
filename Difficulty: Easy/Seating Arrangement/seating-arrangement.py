class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        n = len(seats)
        for i in range(n - 1):
            if seats[i] == 1 and seats[i + 1] == 1:
                return False
                
        if k <= 0:
            return True
            
        for i in range(n):
            if seats[i] == 0:
                left_empty = (i == 0 or seats[i - 1] == 0)
                right_empty = (i == n - 1 or seats[i + 1] == 0)
                
                if left_empty and right_empty:
                    seats[i] = 1  # Occupy the seat
                    k -= 1        # One less person to seat
                    
                    if k <= 0:
                        return True
                        
        return k <= 0