class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_counts = [0] * 37
        
        for i in range(1, n + 1):
            # Calculate sum of digits
            digit_sum = 0
            temp = i
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            sum_counts[digit_sum] += 1
            
        max_size = max(sum_counts)
        
        # Count how many groups have this maximum size
        return sum_counts.count(max_size)
        