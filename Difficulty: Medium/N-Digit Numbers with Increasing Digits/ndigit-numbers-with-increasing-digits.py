class Solution:
    def increasingNumbers(self, n):
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        if n > 9:
            return []
            
        result = []
        
        def backtrack(current_num, last_digit, remaining_digits):
            if remaining_digits == 0:
                result.append(current_num)
                return
            
            for next_digit in range(last_digit + 1, 10):
                backtrack(current_num * 10 + next_digit, next_digit, remaining_digits - 1)
        
        for first_digit in range(1, 10):
            backtrack(first_digit, first_digit, n - 1)
            
        return result
        # code here
