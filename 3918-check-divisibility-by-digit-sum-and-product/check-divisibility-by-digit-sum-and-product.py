class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = [int(d) for d in str(n)]
    
        # Calculate sum of digits
        digit_sum = sum(digits)
        
        # Calculate product of digits
        digit_product = 1
        for d in digits:
            digit_product *= d
            
        # Calculate the divisor
        divisor = digit_sum + digit_product
        
        # Return true if divisible, otherwise false
        return n % divisor == 0