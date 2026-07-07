class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = abs(n)
        non_zero_digits = [d for d in str(n) if d != '0']
        if not non_zero_digits:
            return 0
        x = int("".join(non_zero_digits))
        digit_sum = sum(int(d) for d in non_zero_digits)
        return x * digit_sum
