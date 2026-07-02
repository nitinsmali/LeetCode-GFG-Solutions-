class Solution:
    def divisibleByK(self, arr, k):
        # code here
        n = len(arr)
        
        if n >= k:
            return True
            
        remainders = set()
        
        for num in arr:
            rem = num % k
            if rem == 0:
                return True
                
            new_remainders = {rem}
            for existing_rem in remainders:
                next_rem = (existing_rem + rem) % k
                if next_rem == 0:
                    return True
                new_remainders.add(next_rem)
                
            remainders.update(new_remainders)
            
        return False