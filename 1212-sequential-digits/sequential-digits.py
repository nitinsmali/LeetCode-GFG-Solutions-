class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        digits = "123456789"
        result = []
        
        min_len = len(str(low))
        max_len = len(str(high))
        
        for length in range(min_len, max_len + 1):
            for start in range(10 - length):
                num = int(digits[start : start + length])
                
                if low <= num <= high:
                    result.append(num)
                    
        return result
