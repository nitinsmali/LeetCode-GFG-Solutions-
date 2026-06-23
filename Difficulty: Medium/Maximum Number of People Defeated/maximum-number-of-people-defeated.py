class Solution:
    def maxPeopleDefeated(self, p):
        # code here
        low = 0
        high = int((3*p) **(1/3)) + 2
        
        ans = 0
        
        while low <= high:
            mid = (low+high) // 2
            total_strength = (mid * (mid + 1) * (2 * mid + 1)) // 6
            
            if total_strength <= p:
                ans = mid       # mid people can be defeated
                low = mid + 1   # Try to defeat more people
            else:
                high = mid - 1  # Exceeded strength, reduce target
                
        return ans