class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            # Calculate the product of digits for the current number
            product = 1
            for digit in str(n):
                product *= int(digit)
            
            # Check divisibility
            if product % t == 0:
                return n
            
            # Increment to check the next number
            n += 1
        