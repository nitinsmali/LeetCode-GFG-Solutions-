class Solution:
    def getLastDigit(self, a, b):
        base = int(a)
        exponent = int(b)
        
        if exponent == 0:
            return 1
            
        last_digit_base = base % 10
        
        rem = exponent % 4
        if rem == 0:
            rem = 4
            
        return (last_digit_base ** rem) % 10
